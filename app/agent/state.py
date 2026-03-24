   
from typing import Annotated, Optional, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    # Conversation history
    messages: Annotated[Sequence[BaseMessage], add_messages]
    # Context for the current turn (retrieved from PDF + web if applicable)
    context: list[str]
    # Conversation summary (used for long-running sessions)
    summary: Optional[str]