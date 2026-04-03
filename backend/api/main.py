from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
from backend.agents.orchestrator import run_retention_workflow
import traceback
from dotenv import load_dotenv

# Force override so it prioritizes .env over stale PowerShell variables!
load_dotenv(override=True)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Customer Retention Agentic API")

# Setup CORS to allow Vercel Frontend to communicate with Render Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CustomerProfile(BaseModel):
    customer_id: str
    age: int
    tenure_months: int
    monthly_charges: float
    total_charges: float
    tech_savvy: int
    support_tickets: int
    recent_network_drops: int
    contract_type: int

class AgenticWorkflowResponse(BaseModel):
    customer_id: str
    risk_score: float
    risk_category: str
    shap_values: Dict[str, float]
    key_drivers: List[str]
    recommended_strategy: str
    strategy_reasoning: str
    action_type: str
    simulated_outcome_prob: float
    simulation_reasoning: str
    drafted_message: str
    logs: List[str]
    errors: List[str]

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Agentic AI Retention Service is running"}

@app.post("/api/v1/run-agents", response_model=AgenticWorkflowResponse)
def run_agents(profile: CustomerProfile):
    try:
        # Convert pydantic model to dict
        data = profile.dict()
        
        # Run LangGraph orchestrator
        final_state = run_retention_workflow(data)
        
        # Clean up the hidden features before returning
        if "_scaled_features" in final_state["customer_data"]:
            del final_state["customer_data"]["_scaled_features"]
            
        return AgenticWorkflowResponse(**final_state)
        
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
