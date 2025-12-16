# graph/states/final_summary.py
from graph.state_machine import ChatState

def final_summary(state: ChatState) -> ChatState:
    cart_items = state["cart"].list_items()
    total = state["cart"].get_total()
    state["response"] = f"Resumen final:\nProductos: {cart_items}\nTotal: {total} EUR\nGracias por tu compra, {state.get('name', '')} de {state.get('city', '')}."
    return state
