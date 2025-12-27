# graph/states/ask_city.py
from graph.types import ChatState


def ask_city(state: ChatState) -> ChatState:
    state["response"] = "¿En qué ciudad resides?"
    state["awaiting_city"] = True
    return state
