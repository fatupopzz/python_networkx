# Implementación de Grafos y Algoritmo de Floyd con NetworkX

## Parte 2 de la Hoja de trabajo :)

Esta implementación opcional utiliza Python y la biblioteca NetworkX para resolver el problema de logística planteado en la hoja de trabajo.

![Visualización del grafo](https://github.com/user-attachments/assets/d0f75d57-b2b8-40d0-99d2-e02c56af61ae)

## Descripción

Esta versión del proyecto implementa las mismas funcionalidades que la versión en Java pero aprovecha las ventajas de Python y NetworkX para proporcionar:

- Algoritmos optimizados para grafos
- Visualización interactiva
- Implementación más concisa y legible
- Manejo eficiente de estructuras de datos complejas

El programa utiliza el algoritmo de Floyd-Warshall para encontrar las rutas más cortas entre todas las ciudades, gestionar diferentes condiciones climáticas y calcular el centro del grafo.

## Estructura del Proyecto

```
python_networkx/
├── logistica_nx/
│   ├── __init__.py
│   ├── graph.py         # Clase LogisticaGraph para gestión del grafo
│   ├── algorithms.py    # Implementación de algoritmos (Floyd, centro)
│   └── utils.py         # Funciones de utilidad (visualización, IO)
├── data/
│   └── logistica.txt    # Archivo de datos
├── tests/
│   ├── __init__.py
│   └── test_graph.py    # Pruebas unitarias
├── main.py              # Punto de entrada del programa
└── requirements.txt     # Dependencias
```

## Requisitos

- Python 3.6 o superior
- Bibliotecas:
  - NetworkX (para manejo de grafos)
  - Matplotlib (para visualización)
  - NumPy (para cálculos numéricos)
  - Pytest (para pruebas unitarias)

## Instalación

```bash
# Clonar o descargar el proyecto
cd python_networkx

# Instalar dependencias
pip3 install networkx matplotlib numpy pytest
```

## Uso

```bash
# Ejecutar el programa
python3 main.py
```

El programa presenta un menú interactivo con las siguientes opciones:

1. **Consultar ruta más corta entre ciudades**: Encontrar la ruta óptima entre dos ciudades.
2. **Mostrar centro del grafo**: Identificar la ciudad central óptima para un centro de distribución.
3. **Modificar el grafo**: Añadir/eliminar conexiones entre ciudades.
4. **Mostrar matriz de adyacencia**: Visualizar las conexiones directas entre ciudades.
5. **Cambiar condición climática**: Alternar entre clima normal, lluvia, nieve y tormenta.
6. **Visualizar grafo**: Mostrar representación gráfica del grafo.
7. **Salir**: Terminar el programa.

## Características Destacadas

### Visualización Interactiva
El programa puede mostrar representaciones visuales del grafo completo y resaltar rutas específicas para análisis.

### Algoritmo de Floyd-Warshall Optimizado
Utiliza la implementación optimizada de NetworkX para encontrar todas las rutas más cortas de manera eficiente.

### Modularidad
El código está organizado en módulos bien definidos siguiendo principios de diseño orientado a objetos, lo que facilita su mantenimiento y extensión.

### Validación de Entrada
Todas las entradas del usuario son validadas para garantizar un funcionamiento robusto y evitar errores.

### Pruebas Unitarias
Incluye pruebas automatizadas que verifican el correcto funcionamiento de:
- Operaciones básicas del grafo
- Algoritmo de cálculo de rutas
- Determinación del centro del grafo

## Formato del Archivo logistica.txt

El programa lee un archivo con el siguiente formato:
```
CiudadOrigen CiudadDestino TiempoNormal TiempoLluvia TiempoNieve TiempoTormenta
```

Ejemplo:
```
BuenosAires SaoPaulo 10 15 20 50
Lima Quito 10 12 15 20
```

## Ejecución de Pruebas

```bash
python3 -m pytest tests/
```

## Implementación del Algoritmo de Floyd

A diferencia de la implementación manual en Java, esta versión utiliza la función `nx.floyd_warshall` de NetworkX que:

1. Calcula distancias entre todos los pares de nodos
2. Gestiona eficientemente grafos grandes
3. Aprovecha optimizaciones de rendimiento integradas

## Cálculo del Centro del Grafo

El centro se calcula de manera similar a la versión Java:
1. Encontrar la excentricidad de cada vértice
2. Identificar el vértice con la menor excentricidad
3. Adaptación para manejar grafos no fuertemente conectados

## Autores

Fatima Navarro  
Emilio Chen

*Universidad del Valle de Guatemala*  
*Facultad de Ingeniería - CC2016 Algoritmos y Estructura de Datos*  
*Semestre I - 2025*
