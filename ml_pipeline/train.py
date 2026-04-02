import pandas as pd
import numpy as np
import xgboost as xgb
import shap
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    print("Loading data...")
    df = pd.read_csv('../data/telecom_churn.csv')
    
    # Features and target
    features = ['age', 'tenure_months', 'monthly_charges', 'total_charges', 
                'tech_savvy', 'support_tickets', 'recent_network_drops', 'contract_type']
    X = df[features]
    y = df['churn']
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Convert back to df to keep feature names for SHAP
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=features)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=features)
    
    print("Training XGBoost Model...")
    model = xgb.XGBClassifier(
        n_estimators=100, 
        learning_rate=0.1, 
        max_depth=5, 
        random_state=42,
        use_label_encoder=False,
        eval_metric='logloss'
    )
    model.fit(X_train_scaled, y_train)
    
    print("Evaluating Model...")
    y_pred = model.predict(X_test_scaled)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred))
    
    print("Fitting SHAP explainer...")
    explainer = shap.TreeExplainer(model)
    
    # Save artifacts
    print("Saving artifacts...")
    os.makedirs('../backend/models', exist_ok=True)
    
    with open('../backend/models/model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    with open('../backend/models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
        
    with open('../backend/models/explainer.pkl', 'wb') as f:
        pickle.dump(explainer, f)
        
    # Also save the feature names to ensure order consistency
    with open('../backend/models/features.pkl', 'wb') as f:
        pickle.dump(features, f)
        
    print("Model training complete. Artifacts saved to ../backend/models/")

if __name__ == "__main__":
    train_model()
