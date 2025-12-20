import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from graph.state_machine import app
from models.cart_model import Cart

state = {
    "user_input": "",
    "response": "",
    "cart": Cart(),
    "intent": "",
    "name": None,
    "city": None,
    "awaiting_confirmation": False,
    "awaiting_name": False,
    "awaiting_city": False,
    "chat_finished": False,
}

while True:
    user_input = input("Usuario: ")
    state["user_input"] = user_input

    result = app.invoke(state)
    state.update(result)

    print(state["response"])

    if state.get("chat_finished"):
        print("\nChat finalizado.")
        break

    if state.get("intent") == "EXIT":
        break
