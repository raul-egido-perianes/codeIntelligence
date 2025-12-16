# graph/states/fallback.py
from graph.state_machine import ChatState  # si necesitas ChatState

def fallback(state: ChatState) -> ChatState:
    state["response"] = "Lo siento, no entendí tu mensaje."
    return state
