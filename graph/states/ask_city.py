# graph/states/ask_city.py
from graph.state_machine import ChatState

def ask_city(state: ChatState) -> ChatState:
    state["response"] = "¿En qué ciudad resides?"
    return state
