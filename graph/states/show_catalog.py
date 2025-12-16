from graph.state_machine import ChatState
from models.catalog import get_all_products

def show_catalog(state: ChatState) -> ChatState:
    products = get_all_products()
    
    if not products:
        state["response"] = "No hay productos disponibles."
        return state

    lines = []
    for p in products:
        lines.append(f"{p['id']} - {p['name']} - {p['category']} - {p['description']} - {p['price']:.2f}€\n")
    
    state["response"] = "Productos disponibles:\n" + "\n".join(lines) + "\nEscribe tu próxima acción:\n"
    
    return state
