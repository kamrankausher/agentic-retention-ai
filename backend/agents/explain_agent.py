import pickle
import numpy as np
import pandas as pd
from backend.agents.state import AgentState
import os

_EXPLAINER = None
_FEATURES = None

def get_explainer_artifacts():
    global _EXPLAINER, _FEATURES
    if _EXPLAINER is None:
        base_path = os.path.join(os.path.dirname(__file__), "..", "models")
        with open(os.path.join(base_path, 'explainer.pkl'), 'rb') as f:
            _EXPLAINER = pickle.load(f)
        with open(os.path.join(base_path, 'features.pkl'), 'rb') as f:
            _FEATURES = pickle.load(f)
    return _EXPLAINER, _FEATURES

def run_explainability_agent(state: AgentState) -> AgentState:
    """
    Node function for Explainability Agent. Uses SHAP to extract feature importance.
    """
    print("--- EXPLAINABILITY AGENT ---")
    
    # If risk is very low, we might not need deep explanation, but we'll do it anyway to be exhaustive
    try:
        explainer, features = get_explainer_artifacts()
        
        # Get scaled features back
        scaled_features = state["customer_data"].get("_scaled_features")
        if not scaled_features:
            raise ValueError("Scaled features not found. Run Risk Agent first.")
            
        scaled_df = pd.DataFrame([scaled_features], columns=features)
        
        # Calculate SHAP values
        shap_values = explainer.shap_values(scaled_df)
        
        # For a single prediction, shap_values is an array of shape (n_features,)
        # Some versions of SHAP might return a list for multiclass, XGBoost binary usually returns 2D array or 1D
        
        if isinstance(shap_values, list):
            vals = shap_values[1][0] # Focus on positive class (churn)
        elif len(shap_values.shape) == 2:
            vals = shap_values[0]
        else:
            vals = shap_values
            
        # Create dictionary of Feature -> Contribution
        shap_dict = {feat: float(val) for feat, val in zip(features, vals)}
        state["shap_values"] = shap_dict
        
        # Sort to find top drivers pushing TOWARDS churn (positive SHAP values)
        drivers = sorted(shap_dict.items(), key=lambda x: x[1], reverse=True)
        top_drivers = [f"{feat} ({val:.4f})" for feat, val in drivers[:3] if val > 0]
        
        state["key_drivers"] = top_drivers
        state["logs"].append(f"Explainability Agent: Top drivers identified -> {', '.join([d.split(' ')[0] for d in top_drivers])}")
        
    except Exception as e:
        state["errors"].append(f"Explainability Error: {str(e)}")
        state["shap_values"] = {}
        state["key_drivers"] = []
        
    return state
