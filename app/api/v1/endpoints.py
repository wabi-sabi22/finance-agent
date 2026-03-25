from fastapi import APIRouter
from app.agent.graph import finance_graph

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(user_input: str, session_id: str):
    # Logic gọi LangGraph
    state = {"messages": [("user", user_input)], "context": [], "summary": None}
    result = finance_graph.invoke(state)
    return {"response": result["messages"][-1].content}