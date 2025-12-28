# CHATBOT DE CARRITO DE COMPRA

Este proyecto es un chatbot conversacional en Python que simula el proceso de compra de productos utilizando un carrito.
Permite al usuario ver productos, añadir o eliminar artículos, modificar cantidades y finalizar la compra proporcionando sus datos, en el caso de no saber que acciones se pueden hacer para gestionar la compra, existe la acción 'help' la que te muestra todas las acciones disponibles para el correcto funcionamiento.

El flujo del chatbot está gestionado mediante LangGraph, simulando una máquina de estados conversacional.


## EJECUCIÓN DEL CHATBOT

Para poder ejecutar el proyecto y utilizarlo de manera correcta y efectiva hay que seguir una serie de pasos:
- Crear un entorno virtual:
    python -m venv .venv
    source .venv/bin/activate     # Linux/macOS
    .venv\Scripts\activate        # Windows

- Instalar las dependencias necesarias en el caso de que no esten instaladas:
    pip install -r requirements.txt

- Ejecutar el programa:
    python app/main.py


## EJECUCIÓN DE LOS TESTS

Para poder ejecutar los tests y comprobar el correcto funcionamiento de las funciones implementadas existen diferentes maneras:
- Desde la propia aplicación donde se abre el proyecto haciendo click derecho sobre la carpeta de test y ejecutandolos.

- Ejecutando este comando desde terminal en la carpeta del proyecto:
    python -m pytest -q


## ARQUITECTURA

El chatbot funciona como una máquina de estados conversacional, donde cada acción del usuario determina la siguiente. 
<img width="507" height="113" alt="image" src="https://github.com/user-attachments/assets/4bf2b56d-fc68-413e-96ca-1776510255da" />



En la carpeta "graph" se puede observar una imagen con un pequeño dibujo del grafo diseñado para implementar el proyecto.


## ESTRUCTURA

codeIntelligence/
├── app/
│   ├── main.py                  # Programa principal
│   ├── config.py
│   └── utils.py
├── graph/
│   ├── state_machine.py         # Grafo principal / LangGraph
│   ├── types.py                 # Definición del estado base
│   ├── GRAFO_CHATBOT.png        # Imagen del diagrama del grafo
│   └── states/                  # Nodos / Acciones del chatbot
│       ├── router_state.py
│       ├── start_state.py
│       ├── show_catalog.py
│       ├── edit_cart.py
│       ├── show_cart.py
│       ├── checkout_confirm.py
│       ├── checkout_cancelled.py
│       ├── ask_name.py
│       ├── ask_city.py
│       ├── final_summary.py
│       ├── help.py
│       └── fallback.py
├── models/
│   ├── cart_model.py            # Lógica del carrito
│   └── catalog.py               # Catálogo de productos
├── tests/
│   ├── test_cart_model.py
│   ├── test_catalog.py
│   ├── test_router.py           # Opcional
│   └── test_states.py
└── README.md



## EJEMPLO

Usuario: ver productos
Bot: Aquí tienes los productos disponibles: ...

Usuario: añadir P003 2
Bot: Producto añadido al carrito.

Usuario: ver carrito
Bot: Estos son tus productos...

Usuario: finalizar
Bot: ¿Deseas confirmar la compra? (sí / no)

Usuario: sí
Bot: ¿Cuál es tu nombre?

Usuario: Raul
Bot: ¿En qué ciudad resides?

Usuario: Barcelona
Bot: Gracias Raul. Tu pedido será enviado a Barcelona. ¡Hasta pronto!
