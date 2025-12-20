# graph/types.py
from typing import TypedDict, Optional
from models.cart_model import Cart

class ChatState(TypedDict):
    user_input: str
    response: str
    cart: Cart
    intent: str
    name: Optional[str]
    city: Optional[str]
    awaiting_confirmation: bool
    awaiting_name: bool
    awaiting_city: bool
    chat_finished: bool