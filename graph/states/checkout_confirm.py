# graph/states/checkout_confirm.py
from graph.state_machine import ChatState

def checkout_confirm(state: ChatState) -> ChatState:
    state["response"] = "¿Deseas confirmar tu compra? (sí/no)"
    return state
