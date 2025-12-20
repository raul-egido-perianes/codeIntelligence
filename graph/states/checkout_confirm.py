# graph/states/checkout_confirm.py
from graph.state_machine import ChatState

def checkout_confirm(state: ChatState) -> ChatState:
    state["awaiting_confirmation"] = True
    state["response"] = "¿Deseas confirmar la compra? (sí / no)"
    return state

