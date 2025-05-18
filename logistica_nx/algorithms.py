"""
Módulo con algoritmos para grafos de logística.
"""

import networkx as nx
from typing import Tuple, List, Optional, Dict
import numpy as np


def shortest_path(graph: nx.DiGraph, start: str, end: str) -> Tuple[Optional[List[str]], Optional[float]]:
    """
    Encuentra la ruta más corta entre dos ciudades.
    
    Args:
        graph: Grafo dirigido de NetworkX
        start: Ciudad de origen
        end: Ciudad de destino
    
    Returns:
        Tupla (camino, distancia) o (None, None) si no hay camino
    """
    if start not in graph.nodes or end not in graph.nodes:
        print("Error: Una o ambas ciudades no existen en el grafo.")
        return None, None
    
    try:
        # Usar el algoritmo de camino más corto de NetworkX
        path = nx.shortest_path(graph, source=start, target=end, weight='weight')
        
        # Calcular la distancia total
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += graph[path[i]][path[i+1]]['weight']
        
        return path, total_distance
    
    except nx.NetworkXNoPath:
        print(f"No existe ruta entre {start} y {end}.")
        return None, None


def all_pairs_shortest_paths(graph: nx.DiGraph) -> Dict:
    """
    Implementa el algoritmo de Floyd-Warshall usando NetworkX.
    
    Args:
        graph: Grafo dirigido de NetworkX
    
    Returns:
        Diccionario con las distancias entre todos los pares de nodos
    """
    # Usar el algoritmo de Floyd-Warshall de NetworkX
    return dict(nx.floyd_warshall(graph, weight='weight'))


def find_center(graph: nx.DiGraph) -> Optional[str]:
    """
    Encuentra el centro del grafo (vértice con excentricidad mínima).
    
    Args:
        graph: Grafo dirigido de NetworkX
    
    Returns:
        La ciudad que es el centro del grafo o None si no se puede calcular
    """
    # Verificar que el grafo sea fuertemente conectado
    if not nx.is_strongly_connected(graph):
        print("Advertencia: El grafo no es fuertemente conectado. Se calculará el centro para la componente más grande.")
        # Encontrar la componente fuertemente conectada más grande
        largest_scc = max(nx.strongly_connected_components(graph), key=len)
        subgraph = graph.subgraph(largest_scc).copy()
    else:
        subgraph = graph
    
    # Calcular la excentricidad para cada nodo
    eccentricity = {}
    for node in subgraph.nodes():
        # La excentricidad es la distancia máxima a cualquier otro nodo
        max_distance = 0
        for target in subgraph.nodes():
            if node != target:
                try:
                    distance = nx.shortest_path_length(subgraph, source=node, target=target, weight='weight')
                    max_distance = max(max_distance, distance)
                except nx.NetworkXNoPath:
                    # Si no hay camino, no consideramos este nodo (en un grafo conectado esto no debería ocurrir)
                    continue
        
        eccentricity[node] = max_distance
    
    # Encontrar el nodo con la menor excentricidad
    if eccentricity:
        center = min(eccentricity.items(), key=lambda x: x[1])[0]
        return center
    else:
        return None


def get_adjacency_matrix(graph: nx.DiGraph) -> Tuple[np.ndarray, List[str]]:
    """
    Obtiene la matriz de adyacencia del grafo.
    
    Args:
        graph: Grafo dirigido de NetworkX
    
    Returns:
        Tupla (matriz de adyacencia, lista de nodos)
    """
    # Obtener la lista ordenada de nodos
    nodes = sorted(graph.nodes())
    
    # Crear la matriz de adyacencia
    adj_matrix = np.full((len(nodes), len(nodes)), np.inf)
    
    # Rellenar la matriz con los pesos
    for i, from_node in enumerate(nodes):
        adj_matrix[i, i] = 0  # Diagonal principal a 0
        for j, to_node in enumerate(nodes):
            if graph.has_edge(from_node, to_node):
                adj_matrix[i, j] = graph[from_node][to_node]['weight']
    
    return adj_matrix, nodes
