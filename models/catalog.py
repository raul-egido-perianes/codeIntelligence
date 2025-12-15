# models/catalog.py
# Catálogo de productos de la tienda

CATALOG = [
    {
        "id": "P001",
        "name": "Camiseta básica",
        "description": "Camiseta de algodón cómoda para uso diario",
        "price": 14.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P002",
        "name": "Pantalón vaquero",
        "description": "Pantalón vaquero azul de corte clásico",
        "price": 29.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P003",
        "name": "Sudadera con capucha",
        "description": "Sudadera cálida ideal para climas frescos",
        "price": 39.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P004",
        "name": "Zapatillas deportivas",
        "description": "Zapatillas comodas perfectas para uso diario",
        "price": 49.99,
        "currency": "EUR",
        "category": "calzado",
    },
    {
        "id": "P005",
        "name": "Botas de montaña",
        "description": "Botas resistentes para senderismo y trekking",
        "price": 89.99,
        "currency": "EUR",
        "category": "calzado",
    },
    {
        "id": "P006",
        "name": "Sandalias de verano",
        "description": "Sandalias ligeras ideales para días calurosos",
        "price": 19.99,
        "currency": "EUR",
        "category": "calzado",
    },
    {
        "id": "P007",
        "name": "Chaqueta impermeable",
        "description": "Chaqueta resistente al agua y al viento",
        "price": 59.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P008",
        "name": "Mochila urbana",
        "description": "Mochila práctica para uso diario y viajes cortos",
        "price": 34.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P009",
        "name": "Gorra deportiva",
        "description": "Gorra ajustable para actividades al aire libre",
        "price": 12.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P010",
        "name": "Calcetines deportivos",
        "description": "Pack de calcetines transpirables",
        "price": 9.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P011",
        "name": "Reloj digital",
        "description": "Reloj digital resistente al agua",
        "price": 44.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P012",
        "name": "Cinturón de cuero",
        "description": "Cinturón clásico de cuero auténtico",
        "price": 22.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P013",
        "name": "Gafas de sol",
        "description": "Gafas de sol con protección UV",
        "price": 18.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P014",
        "name": "Pijama cómodo",
        "description": "Pijama suave para descanso nocturno",
        "price": 24.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P015",
        "name": "Zapatillas de casa",
        "description": "Zapatillas suaves para estar en casa",
        "price": 16.99,
        "currency": "EUR",
        "category": "calzado",
    },
    {
        "id": "P016",
        "name": "Bolso de mano",
        "description": "Bolso elegante para uso diario",
        "price": 45.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P017",
        "name": "Camiseta deportiva",
        "description": "Camiseta transpirable para entrenamientos",
        "price": 19.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P018",
        "name": "Pantalón deportivo",
        "description": "Pantalón cómodo para actividad física",
        "price": 27.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P019",
        "name": "Riñonera",
        "description": "Riñonera ligera para llevar lo esencial",
        "price": 14.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P020",
        "name": "Bufanda de invierno",
        "description": "Bufanda cálida para días fríos",
        "price": 17.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P021",
        "name": "Guantes térmicos",
        "description": "Guantes térmicos para bajas temperaturas",
        "price": 21.99,
        "currency": "EUR",
        "category": "accesorios",
    },
    {
        "id": "P022",
        "name": "Zapatillas running",
        "description": "Zapatillas ligeras para correr",
        "price": 69.99,
        "currency": "EUR",
        "category": "calzado",
    },
    {
        "id": "P023",
        "name": "Camisa formal",
        "description": "Camisa elegante para ocasiones formales",
        "price": 34.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P024",
        "name": "Polo clásico",
        "description": "Polo de algodón de estilo clásico",
        "price": 23.99,
        "currency": "EUR",
        "category": "ropa",
    },
    {
        "id": "P025",
        "name": "Maleta de viaje",
        "description": "Maleta resistente para viajes largos",
        "price": 99.99,
        "currency": "EUR",
        "category": "accesorios",
    },
]


# Devuelve todos los productos del catálogo
def get_all_products():
    return CATALOG

# Devuelve el producto a partir de la ID
def get_product_by_id(product_id: str):
    return next((p for p in CATALOG if p["id"] == product_id), None)


# Devuelve el producto buscado por nombre
def search_products_by_name(text: str):
    text = text.lower()
    return [p for p in CATALOG if text in p["name"].lower()]
