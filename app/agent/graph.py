from langgraph.graph import StateGraph, END
from app.agent.state import AgentState
from app.agent.nodes import smart_rag_node

def build_graph():
    workflow = StateGraph(AgentState)
    
    # Use a single node for maximum performance/latency efficiency
    workflow.add_node("agent", smart_rag_node)
    
    workflow.set_entry_point("agent")
    workflow.add_edge("agent", END)
    
    return workflow.compile()

finance_graph = build_graph()