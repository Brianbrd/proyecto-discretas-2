# Matemáticas Discretas II - Proyecto Entrega 1

## Descripción del Proyecto
Este proyecto consiste en la implementación básica de grafos dirigidos y no dirigidos en Python desde cero. Incluye funciones para leer los datos desde archivos CSV (`source,target,weight`) y verificar si un grafo es conexo, si tiene ciclos, si es un árbol o si es un bosque.

## Elección de Representación de Grafo
Decidí usar Listas de Adyacencia por curiosidad, ya que quería experimentar cómo funcionaba esta estructura en la práctica y ver qué pasaba al construir las conexiones de los nodos de esta manera en lugar de usar una matriz tradicional. Aunque el otro método también habría sido interesante, me decanté por este método.

## ¿Cómo me fue?
Al principio fue un reto configurar todo el ambiente con `uv` y conectar el repositorio en GitHub desde la terminal, pero ir paso a paso me permitió entender cómo se estructura un proyecto real en Python. Implementar los recorridos para detectar ciclos y verificar si el grafo era conexo ayudó a conectar con la teoría vista en clase.

## Ejecución
Para ejecutar las pruebas del proyecto utilizando `uv`, correr en la terminal:
```bash
uv run main.py