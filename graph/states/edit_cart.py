# graph/states/edit_cart.py
from graph.types import ChatState

def edit_cart(state: ChatState) -> ChatState:
    user_input = state["user_input"].lower().strip()
    cart = state["cart"]
    parts = user_input.split()

    if not parts:
        state["response"] = "No se entendió tu acción. Intenta de nuevo."
        return state

    action = parts[0]

    if action == "añadir" and len(parts) == 3:
        product_id = parts[1].upper()
        try:
            quantity = int(parts[2])
            existing = cart.get_item(product_id)
            if existing:
                existing.quantity += quantity
                msg = f"El producto '{product_id}' ya estaba en el carrito. Se sumó la cantidad, ahora tienes {existing.quantity}."
            else:
                cart.add_product(product_id, quantity)
                msg = f"Producto '{product_id}' añadido al carrito."
            state["response"] = msg + "\nEscribe tu próxima acción:"
        except ValueError:
            state["response"] = "Cantidad inválida. Ejemplo: 'añadir P001 2'."

    elif action == "modificar" and len(parts) == 3:
        product_id = parts[1].upper()
        try:
            quantity = int(parts[2])
            item = cart.get_item(product_id)
            if item:
                cart.update_quantity(product_id, quantity)
                state["response"] = f"La cantidad de '{product_id}' se actualizó a {quantity}."
            else:
                state["response"] = f"El producto '{product_id}' no está en el carrito."
        except ValueError:
            state["response"] = "Cantidad inválida. Ejemplo: 'modificar P001 3'."

    elif action in ("eliminar", "quitar") and len(parts) == 2:
        product_id = parts[1].upper()
        item = cart.get_item(product_id)
        if item:
            cart.remove_product(product_id)
            state["response"] = f"El producto '{product_id}' fue eliminado del carrito."
        else:
            state["response"] = f"El producto '{product_id}' no está en el carrito."

    else:
        state["response"] = (
            "Comando no reconocido. Usa:\n"
            "- 'añadir P001 2'\n"
            "- 'modificar P001 3'\n"
            "- 'eliminar P001'"
        )

    return state
