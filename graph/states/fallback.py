# graph/states/fallback.py
from graph.types import ChatState

def fallback(state: ChatState) -> ChatState:
    state["response"] = "Lo siento, no entendí tu mensaje."
    return state
