# graph/states/final_summary.py
from graph.state_machine import ChatState

def final_summary(state: ChatState) -> ChatState:
    cart_items = state["cart"].list_items()
    total = state["cart"].get_total()
    state["response"] = (
        f"Gracias {state['name']}.\n"
        f"Tu pedido se enviará a {state['city']}.\n"
        f"Total: {total:.2f} €\n"
        f"¡Hasta pronto!"
    )

    state["chat_finished"] = True

    return state
