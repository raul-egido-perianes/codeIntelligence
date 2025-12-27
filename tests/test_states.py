# tests/test_states.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from graph.states.checkout_confirm import checkout_confirm
from graph.states.checkout_cancelled import checkout_cancelled
from graph.states.ask_name import ask_name
from graph.states.ask_city import ask_city
from graph.states.final_summary import final_summary
from models.cart_model import Cart

def test_checkout_confirm():
    state = {"cart": Cart()}
    result = checkout_confirm(state)
    assert result["response"].startswith("¿Deseas confirmar")
    assert result["awaiting_confirmation"] is True

def test_checkout_cancelled():
    state = {}
    result = checkout_cancelled(state)
    assert "cancelada" in result["response"]
