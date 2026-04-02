from langgraph.graph import StateGraph, END
from backend.agents.state import AgentState
from backend.agents.risk_agent import run_risk_agent
from backend.agents.explain_agent import run_explainability_agent
from backend.agents.strategy_agent import run_strategy_agent
from backend.agents.simulation_agent import run_simulation_agent
from backend.agents.communication_agent import run_communication_agent

def build_graph():
    """
    Builds the Agentic workflow using LangGraph.
    """
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("risk_agent", run_risk_agent)
    workflow.add_node("explainability_agent", run_explainability_agent)
    workflow.add_node("strategy_agent", run_strategy_agent)
    workflow.add_node("simulation_agent", run_simulation_agent)
    workflow.add_node("communication_agent", run_communication_agent)
    
    # Define edges
    # Risk is the entry point
    workflow.set_entry_point("risk_agent")
    
    # Simple linear flow for this pipeline
    workflow.add_edge("risk_agent", "explainability_agent")
    workflow.add_edge("explainability_agent", "strategy_agent")
    workflow.add_edge("strategy_agent", "simulation_agent")
    workflow.add_edge("simulation_agent", "communication_agent")
    workflow.add_edge("communication_agent", END)
    
    # Compile the graph
    app = workflow.compile()
    return app

def run_retention_workflow(customer_data: dict) -> AgentState:
    """
    Initializes state and runs the workflow.
    """
    app = build_graph()
    
    initial_state = AgentState(
        customer_id=customer_data.get("customer_id", "UNKNOWN"),
        customer_data=customer_data,
        risk_score=0.0,
        risk_category="",
        shap_values={},
        key_drivers=[],
        recommended_strategy="",
        strategy_reasoning="",
        action_type="",
        simulated_outcome_prob=0.0,
        simulation_reasoning="",
        drafted_message="",
        logs=["Workflow initialized"],
        errors=[]
    )
    
    # Execute graph
    # Depending on LangGraph version, invoke usually expects a dict matching TypedDict
    final_state = app.invoke(initial_state)
    return final_state
