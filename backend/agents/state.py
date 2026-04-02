from typing import TypedDict, List, Dict, Any, Optional

class AgentState(TypedDict):
    """
    Represents the state of our agentic workflow.
    """
    customer_id: str
    customer_data: Dict[str, Any]
    
    # Outputs from Risk Agent
    risk_score: float
    risk_category: str  # "LOW", "MEDIUM", "HIGH"
    
    # Outputs from Explainability Agent
    shap_values: Dict[str, float]
    key_drivers: List[str]
    
    # Outputs from Strategy Agent
    recommended_strategy: str
    strategy_reasoning: str
    action_type: str # e.g., "DISCOUNT", "CALL", "EMAIL", "NO_ACTION"
    
    # Outputs from Simulation Agent
    simulated_outcome_prob: float
    simulation_reasoning: str
    
    # Outputs from Communication Agent
    drafted_message: str
    
    # Any global errors or logs
    logs: List[str]
    errors: List[str]
