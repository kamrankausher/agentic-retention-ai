import pickle
import pandas as pd
from typing import Dict, Any
from backend.agents.state import AgentState
import os

# Lazy load models to avoid circular dependencies and slow startup
_MODEL = None
_SCALER = None
_FEATURES = None

def get_ml_artifacts():
    global _MODEL, _SCALER, _FEATURES
    if _MODEL is None:
        base_path = os.path.join(os.path.dirname(__file__), "..", "models")
        
        with open(os.path.join(base_path, 'model.pkl'), 'rb') as f:
            _MODEL = pickle.load(f)
            
        with open(os.path.join(base_path, 'scaler.pkl'), 'rb') as f:
            _SCALER = pickle.load(f)
            
        with open(os.path.join(base_path, 'features.pkl'), 'rb') as f:
            _FEATURES = pickle.load(f)
            
    return _MODEL, _SCALER, _FEATURES

def run_risk_agent(state: AgentState) -> AgentState:
    """
    Node function for Risk Agent. Validates input and gets prediction.
    """
    print("--- RISK AGENT ---")
    customer_data = state["customer_data"]
    
    try:
        model, scaler, features = get_ml_artifacts()
        
        # Build dataframe for inference
        df = pd.DataFrame([customer_data])
        
        # Ensure correct column order
        df = df[features]
        
        # Scale
        scaled_data = scaler.transform(df)
        scaled_df = pd.DataFrame(scaled_data, columns=features)
        
        # Predict Prob
        probs = model.predict_proba(scaled_df)
        churn_prob = float(probs[0][1])  # Class 1 prob
        
        # Categorize
        if churn_prob < 0.3:
            category = "LOW"
        elif churn_prob < 0.7:
            category = "MEDIUM"
        else:
            category = "HIGH"
            
        state["risk_score"] = churn_prob
        state["risk_category"] = category
        state["logs"].append(f"Risk Agent: Score {churn_prob:.2f} ({category})")
        
        # Store scaled_df in data for explainer to use quickly
        state["customer_data"]["_scaled_features"] = scaled_data.tolist()[0]
        
    except Exception as e:
        state["errors"].append(f"Risk Agent Error: {str(e)}")
        state["risk_score"] = 0.0
        state["risk_category"] = "UNKNOWN"
        
    return state
