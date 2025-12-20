# graph/states/checkout_cancelled.py
from graph.types import ChatState

def checkout_cancelled(state: ChatState) -> ChatState:
    state["response"] = "Compra cancelada. ¿En qué más puedo ayudarte?"
    state["intent"] = "IDLE"
    return state
