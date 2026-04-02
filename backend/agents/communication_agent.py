import json
import os
from openai import OpenAI
from pydantic import BaseModel
from backend.agents.state import AgentState

class CommunicationOutput(BaseModel):
    drafted_message: str

def run_communication_agent(state: AgentState) -> AgentState:
    """
    Node function for Communication Agent. Drafts the email/sms using Grok.
    """
    print("--- COMMUNICATION AGENT ---")
    
    if state.get("action_type") == "NO_ACTION":
        state["drafted_message"] = ""
        state["logs"].append("Communication Agent: Skipped due to NO_ACTION.")
        return state
        
    try:
        client = OpenAI(
            api_key=os.environ.get("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
        
        prompt = f"""
        You are an expert Copywriter for a telecom company.
        
        Customer Profile:
        {json.dumps({k:v for k,v in state['customer_data'].items() if not k.startswith('_')})}
        
        Action Type Chosen: {state.get('action_type', '')}
        Reasoning: {state.get('strategy_reasoning', '')}
        
        Task: Draft a highly personalized, empathetic, and professional message (email or SMS depending on what fits best) to this customer to execute the strategy. 
        Do not mention "churn" or "risk score" to the customer. Frame it as a proactive customer service gesture to improve their experience.
        Keep it concise, premium, and friendly.
        
        IMPORTANT: Your output MUST be in valid JSON format matching this schema:
        {{
            "drafted_message": "string"
        }}
        """
        
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        output = json.loads(response.choices[0].message.content)
        
        state["drafted_message"] = output.get("drafted_message", "")
        state["logs"].append("Communication Agent: Drafted retention message.")
        
    except Exception as e:
        state["errors"].append(f"Communication Error: {str(e)}")
        state["drafted_message"] = "Error drafting message."
        
    return state
