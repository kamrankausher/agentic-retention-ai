import json
import os
from openai import OpenAI
from pydantic import BaseModel
from backend.agents.state import AgentState

class StrategyOutput(BaseModel):
    recommended_strategy: str
    action_type: str
    reasoning: str

def run_strategy_agent(state: AgentState) -> AgentState:
    """
    Node function for Strategy Agent. Uses Grok to determine the best retention strategy.
    """
    print("--- STRATEGY AGENT ---")
    
    if state.get("risk_category") == "LOW":
        state["recommended_strategy"] = "No intervention needed"
        state["action_type"] = "NO_ACTION"
        state["strategy_reasoning"] = "Customer is at very low risk of churning."
        state["logs"].append("Strategy Agent: Skipped due to LOW risk.")
        return state
        
    try:
        client = OpenAI(
            api_key=os.environ.get("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
        
        customer_profile = state["customer_data"]
        clean_profile = {k: v for k, v in customer_profile.items() if not k.startswith('_')}
        
        prompt = f"""
        You are an elite Business Strategy AI at a top telecom company.
        Your goal is to decide the best actionable strategy to retain a customer who is at risk of churning.
        
        Here is the customer profile:
        {json.dumps(clean_profile, indent=2)}
        
        Risk Score: {state.get('risk_score', 0):.2f} ({state.get('risk_category', 'UNKNOWN')})
        Top factors pushing this customer to churn (from SHAP analysis):
        {json.dumps(state.get('key_drivers', []), indent=2)}
        
        Select exactly ONE action_type from this list: ["DISCOUNT", "TECH_SUPPORT_CALL", "FREE_UPGRADE", "EMAIL_CHECKIN"]
        
        Provide your reasoning focusing on the SHAP factors and customer profile (e.g. if 'recent_network_drops' is high, suggest TECH_SUPPORT_CALL or FREE_UPGRADE to better hardware).
        Be concise and strategic.
        
        IMPORTANT: Your output MUST be in valid JSON format matching this schema:
        {{
            "recommended_strategy": "string",
            "action_type": "string",
            "reasoning": "string"
        }}
        """
        
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        output = json.loads(response.choices[0].message.content)
        
        state["recommended_strategy"] = output.get("recommended_strategy", "")
        state["action_type"] = output.get("action_type", "EMAIL_CHECKIN")
        state["strategy_reasoning"] = output.get("reasoning", "")
        state["logs"].append(f"Strategy Agent: Chose action '{state['action_type']}'")
        
    except Exception as e:
        state["errors"].append(f"Strategy Error: {str(e)}")
        state["recommended_strategy"] = "Fallback: General Check-in"
        state["action_type"] = "EMAIL_CHECKIN"
        state["strategy_reasoning"] = f"Failed to generate strategy. Returning fallback. Error: {str(e)}"
        
    return state
