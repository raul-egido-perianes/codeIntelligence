# models/cart_model.py

from typing import List, Dict, Optional
from models.catalog import get_product_by_id

class CartProduct:
    def __init__(self, product: Dict, quantity: int):
        self.product = product
        self.quantity = quantity
    
    def get_subtotal(self) -> float:
        return self.product["price"] * self.quantity


class Cart:
    def __init__(self):
        self.items: List[CartProduct] = []
    
    def add_product(self, product_id: str, quantity: int) -> str:
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        
        product = get_product_by_id(product_id)
        if not product:
            raise ValueError(f"El producto con ID '{product_id}' no existe en el catálogo.")

        existing_item = self.get_item(product_id)
        if existing_item:
            existing_item.quantity += quantity
            return f"El producto '{product['name']}' ya estaba en el carro. Se ha sumado la cantidad, ahora tienes {existing_item.quantity}."
        else:
            self.items.append(CartProduct(product, quantity))
            return f"Se ha añadido '{product['name']}' al carro con cantidad {quantity}."
    
    def remove_product(self, product_id: str):
        item = self.get_item(product_id)
        if item:
            self.items.remove(item)

    def update_quantity(self, product_id: str, quantity: int):
        item = self.get_item(product_id)
        if item:
            if quantity <= 0:
                self.remove_product(product_id)
            else:
                item.quantity = quantity
    
    def get_total(self) -> float:
        return sum(item.get_subtotal() for item in self.items)

    def get_item(self, product_id: str) -> Optional[CartProduct]:
        for item in self.items:
            if item.product["id"] == product_id:
                return item
        return None
    
    def list_items(self) -> List[Dict]:
        return [
            {
                "id": item.product["id"],
                "name": item.product["name"],
                "price": item.product["price"],
                "quantity": item.quantity,
                "subtotal": item.get_subtotal()
            }
            for item in self.items
        ]
