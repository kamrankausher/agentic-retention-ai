import json
import os
from openai import OpenAI
from pydantic import BaseModel
from backend.agents.state import AgentState

class SimulationOutput(BaseModel):
    simulated_outcome_prob: float
    simulation_reasoning: str

def run_simulation_agent(state: AgentState) -> AgentState:
    """
    Node function for Simulation Agent. Predicts the effectiveness of the proposed strategy using Grok.
    """
    print("--- SIMULATION AGENT ---")
    
    if state.get("action_type") == "NO_ACTION":
        state["simulated_outcome_prob"] = state.get("risk_score", 0.0)
        state["simulation_reasoning"] = "No action taken. Risk remains the same."
        state["logs"].append("Simulation Agent: Skipped due to NO_ACTION.")
        return state
        
    try:
        client = OpenAI(
            api_key=os.environ.get("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
        
        prompt = f"""
        You are an advanced Customer Analytics Simulator.
        
        Customer Profile:
        {json.dumps({k:v for k,v in state['customer_data'].items() if not k.startswith('_')})}
        
        Current Risk Score of Churning: {state.get('risk_score', 0):.2f}
        Primary friction points (SHAP factors): {state.get('key_drivers', [])}
        
        Proposed Intervention:
        Action Type: {state.get('action_type', '')}
        Strategy: {state.get('recommended_strategy', '')}
        
        Task: Simulate the outcome. If we apply this intervention, what is the new probability that the customer will churn? 
        The intervention should theoretically lower the probability, but how much depends on the friction points.
        For example, a discount won't completely solve network drops, but a tech call might.
        
        IMPORTANT: Your output MUST be in valid JSON format matching this schema:
        {{
            "simulated_outcome_prob": float (between 0.0 and 1.0),
            "simulation_reasoning": "string"
        }}
        """
        
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        output = json.loads(response.choices[0].message.content)
        
        state["simulated_outcome_prob"] = output.get("simulated_outcome_prob", state.get("risk_score", 0))
        state["simulation_reasoning"] = output.get("simulation_reasoning", "")
        state["logs"].append(f"Simulation Agent: Predicted improved risk score -> {state['simulated_outcome_prob']:.2f}")
        
    except Exception as e:
        state["errors"].append(f"Simulation Error: {str(e)}")
        state["simulated_outcome_prob"] = state.get("risk_score", 0.0)
        state["simulation_reasoning"] = "Simulation failed due to an error."
        
    return state
