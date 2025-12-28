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

<img width="427" height="490" alt="image" src="https://github.com/user-attachments/assets/f8e6ff8a-dfc3-4cca-976d-d7ad7e321e14" />




## EJEMPLO

Usuario: ver productos <br>
Bot: Aquí tienes los productos disponibles: ...

Usuario: añadir P003 2 <br>
Bot: Producto añadido al carrito.

Usuario: ver carrito <br>
Bot: Estos son tus productos...

Usuario: finalizar <br>
Bot: ¿Deseas confirmar la compra? (sí / no)

Usuario: sí <br>
Bot: ¿Cuál es tu nombre?

Usuario: Raul <br>
Bot: ¿En qué ciudad resides?

Usuario: Barcelona <br>
Bot: Gracias Raul. Tu pedido será enviado a Barcelona. ¡Hasta pronto!
