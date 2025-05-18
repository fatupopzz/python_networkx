"""
Módulo con funciones de utilidad para visualización y manejo de datos.
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional


def visualize_graph(graph: nx.DiGraph, path: Optional[List[str]] = None, 
                   title: str = "Grafo de Logística") -> None:
    """
    Visualiza el grafo y opcionalmente resalta una ruta.
    
    Args:
        graph: Grafo dirigido de NetworkX
        path: Lista opcional de ciudades que forman una ruta a resaltar
        title: Título del gráfico
    """
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)  # Posición de los nodos
    
    # Dibujar los nodos y aristas
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue', alpha=0.8)
    
    # Extraer pesos para el grosor de las aristas
    edge_weights = [graph[u][v]['weight'] for u, v in graph.edges()]
    max_weight = max(edge_weights) if edge_weights else 1
    
    # Normalizar los pesos para el grosor de las aristas (inversamente proporcional)
    normalized_weights = [1 + 3 * (1 - (w / max_weight)) for w in edge_weights]
    
    # Dibujar aristas con grosor basado en el peso (inversamente proporcional)
    nx.draw_networkx_edges(graph, pos, width=normalized_weights, alpha=0.7, 
                          edge_color='gray', arrows=True, arrowsize=15)
    
    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
    
    # Preparar etiquetas de aristas con los pesos
    edge_labels = {(u, v): f"{attrs['weight']:.1f}" for u, v, attrs in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)
    
    # Resaltar una ruta si se proporciona
    if path and len(path) > 1:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, width=3, alpha=1, 
                              edge_color='red', arrows=True, arrowsize=20)
        
        # Resaltar los nodos en la ruta
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_size=700, 
                               node_color='lightcoral', alpha=1)
    
    plt.title(title)
    plt.axis('off')  # Ocultar ejes
    plt.tight_layout()
    
    # Mostrar el gráfico
    plt.show()


def print_adjacency_matrix(adj_matrix: np.ndarray, nodes: List[str]) -> None:
    """
    Imprime la matriz de adyacencia del grafo.
    
    Args:
        adj_matrix: Matriz de adyacencia (numpy array)
        nodes: Lista de nombres de los nodos
    """
    print("\nMatriz de Adyacencia:")
    print(f"{'':15}", end="")
    for node in nodes:
        print(f"{node:15}", end="")
    print()
    
    for i, from_node in enumerate(nodes):
        print(f"{from_node:15}", end="")
        for j in range(len(nodes)):
            if adj_matrix[i, j] == np.inf:
                print(f"{'∞':15}", end="")
            else:
                print(f"{adj_matrix[i, j]:15.2f}", end="")
        print()


def validate_float_input(prompt: str) -> float:
    """
    Solicita y valida un número flotante.
    
    Args:
        prompt: Mensaje para mostrar al usuario
    
    Returns:
        float: El número validado
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Por favor, ingrese un número válido.")


def validate_menu_option(prompt: str, min_value: int, max_value: int) -> int:
    """
    Solicita y valida una opción de menú.
    
    Args:
        prompt: Mensaje para mostrar al usuario
        min_value: Valor mínimo aceptable
        max_value: Valor máximo aceptable
    
    Returns:
        int: La opción validada
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Por favor, ingrese un número entre {min_value} y {max_value}.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
