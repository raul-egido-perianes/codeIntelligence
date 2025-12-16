# graph/states/show_cart.py
from graph.types import ChatState  # o desde donde tengas ChatState

def show_cart(state: ChatState) -> ChatState:
    cart = state["cart"].list_items()

    if not cart:
        state["response"] = "No hay productos en el carro.\nEscribe 'añadir <ID> <cantidad>' para agregar productos.\n"
        return state
    
    lines = []
    for item in cart:
        lines.append(f"{item['id']} - {item['name']} - {item['price']:.2f}€ x{item['quantity']}")

    state["response"] = "Productos disponibles en el carro:\n" + "\n".join(lines) + "\nEscribe tu próxima acción:\n"

    return state

