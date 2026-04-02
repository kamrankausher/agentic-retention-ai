import pandas as pd
import numpy as np
import os

def generate_telecom_data(num_samples=2000):
    np.random.seed(42)
    
    # Customer Demographics
    age = np.random.randint(18, 75, num_samples)
    tenure_months = np.random.randint(1, 72, num_samples)
    
    # Financials
    monthly_charges = np.random.uniform(20.0, 120.0, num_samples)
    # Total charges is approximately tenure * monthly charges + some noise
    total_charges = tenure_months * monthly_charges * np.random.uniform(0.9, 1.1, num_samples)
    
    # Service Usage Profile
    # Tech savvy users typically have lower churn unless support tickets are high
    tech_savvy = np.random.choice([0, 1], num_samples, p=[0.6, 0.4])
    
    # Support & Issues
    support_tickets_opened = np.random.poisson(lam=0.5, size=num_samples)
    recent_drops = np.random.poisson(lam=1.5, size=num_samples)
    
    # Contract type: 0 = Month-to-Month, 1 = One Year, 2 = Two Year
    contract_type = np.random.choice([0, 1, 2], num_samples, p=[0.5, 0.3, 0.2])
    
    # Define churn rule (more likely to churn if month-to-month, high drops, many support tickets, short tenure)
    # We will simulate a probability and then sample
    churn_prob = np.zeros(num_samples)
    
    # Base churn prob
    churn_prob += 0.1
    
    # Factors increasing churn
    churn_prob += (contract_type == 0) * 0.3  # Month-to-month is higher risk
    churn_prob += (recent_drops > 3) * 0.2
    churn_prob += (support_tickets_opened > 1) * 0.15
    churn_prob += (monthly_charges > 80) * 0.1
    
    # Factors decreasing churn
    churn_prob -= (tenure_months > 24) * 0.2
    churn_prob -= (contract_type == 2) * 0.3
    churn_prob -= tech_savvy * 0.05
    
    # Clip prob and sample
    churn_prob = np.clip(churn_prob, 0.05, 0.95)
    churn = np.random.binomial(1, churn_prob)
    
    df = pd.DataFrame({
        'customer_id': [f"CUST_{i:04d}" for i in range(num_samples)],
        'age': age,
        'tenure_months': tenure_months,
        'monthly_charges': monthly_charges,
        'total_charges': total_charges,
        'tech_savvy': tech_savvy,
        'support_tickets': support_tickets_opened,
        'recent_network_drops': recent_drops,
        'contract_type': contract_type,
        'churn': churn
    })
    
    os.makedirs('../data', exist_ok=True)
    df.to_csv('../data/telecom_churn.csv', index=False)
    print(f"Generated {num_samples} samples and saved to ../data/telecom_churn.csv")
    print(df['churn'].value_counts())

if __name__ == "__main__":
    generate_telecom_data()
