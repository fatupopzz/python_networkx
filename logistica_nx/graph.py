"""
Módulo para la gestión de grafos de logística usando NetworkX.
"""

import networkx as nx
from typing import Optional, Dict, Any


class LogisticaGraph:
    """Clase para representar y gestionar un grafo de logística."""
    
    def __init__(self):
        """Inicializa un grafo dirigido vacío."""
        self.graph = nx.DiGraph()
        self.current_weather = "normal"  # Clima por defecto
    
    def load_from_file(self, filename: str) -> bool:
        """
        Carga un grafo desde un archivo.
        
        Args:
            filename: Ruta al archivo de datos
            
        Returns:
            bool: True si la carga fue exitosa, False en caso contrario
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) >= 6:
                        from_city = parts[0]
                        to_city = parts[1]
                        normal_time = float(parts[2])
                        rain_time = float(parts[3])
                        snow_time = float(parts[4])
                        storm_time = float(parts[5])
                        
                        # Agregar nodos si no existen
                        if not self.graph.has_node(from_city):
                            self.graph.add_node(from_city)
                        if not self.graph.has_node(to_city):
                            self.graph.add_node(to_city)
                        
                        # Agregar arista con todos los tiempos como atributos
                        self.graph.add_edge(from_city, to_city, 
                                           normal=normal_time, 
                                           rain=rain_time, 
                                           snow=snow_time, 
                                           storm=storm_time,
                                           weight=normal_time)  # Peso por defecto
            
            print(f"Grafo cargado exitosamente con {self.graph.number_of_nodes()} ciudades y {self.graph.number_of_edges()} conexiones.")
            return True
        
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo '{filename}'")
            return False
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return False
    
    def save_to_file(self, filename: str) -> bool:
        """
        Guarda el grafo en un archivo.
        
        Args:
            filename: Ruta al archivo de destino
            
        Returns:
            bool: True si la escritura fue exitosa, False en caso contrario
        """
        try:
            with open(filename, 'w') as file:
                for u, v, data in self.graph.edges(data=True):
                    file.write(f"{u} {v} {data['normal']} {data['rain']} {data['snow']} {data['storm']}\n")
            
            print(f"Grafo guardado exitosamente en '{filename}'")
            return True
        
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            return False
    
    def set_weather(self, weather_type: str) -> bool:
        """
        Cambia la condición climática actual del grafo.
        
        Args:
            weather_type: Tipo de clima ('normal', 'rain', 'snow', 'storm')
            
        Returns:
            bool: True si el cambio fue exitoso, False en caso contrario
        """
        valid_weather = ['normal', 'rain', 'snow', 'storm']
        if weather_type not in valid_weather:
            print(f"Clima no válido. Opciones: {', '.join(valid_weather)}")
            return False
        
        self.current_weather = weather_type
        
        # Actualizar el peso de cada arista según el clima seleccionado
        for u, v, attrs in self.graph.edges(data=True):
            self.graph[u][v]['weight'] = attrs[weather_type]
        
        print(f"Clima cambiado a: {weather_type}")
        return True
    
    def add_city(self, city_name: str) -> bool:
        """
        Agrega una nueva ciudad al grafo.
        
        Args:
            city_name: Nombre de la ciudad
        
        Returns:
            bool: True si la ciudad se agregó correctamente, False si ya existía
        """
        if city_name in self.graph.nodes():
            print(f"La ciudad '{city_name}' ya existe en el grafo.")
            return False
        
        self.graph.add_node(city_name)
        print(f"Ciudad '{city_name}' agregada correctamente.")
        return True
    
    def add_connection(self, from_city: str, to_city: str, times: Dict[str, float]) -> bool:
        """
        Agrega una conexión entre dos ciudades.
        
        Args:
            from_city: Ciudad de origen
            to_city: Ciudad de destino
            times: Diccionario con los tiempos para cada clima
            
        Returns:
            bool: True si la conexión se agregó correctamente
        """
        # Asegurarse de que las ciudades existan
        if from_city not in self.graph.nodes():
            self.add_city(from_city)
        
        if to_city not in self.graph.nodes():
            self.add_city(to_city)
        
        # Agregar la conexión
        self.graph.add_edge(from_city, to_city, 
                           normal=times['normal'], 
                           rain=times['rain'], 
                           snow=times['snow'], 
                           storm=times['storm'],
                           weight=times[self.current_weather])
        
        print(f"Conexión de {from_city} a {to_city} agregada correctamente.")
        return True
    
    def remove_connection(self, from_city: str, to_city: str) -> bool:
        """
        Elimina una conexión entre dos ciudades.
        
        Args:
            from_city: Ciudad de origen
            to_city: Ciudad de destino
            
        Returns:
            bool: True si la conexión se eliminó correctamente
        """
        if from_city not in self.graph.nodes() or to_city not in self.graph.nodes():
            print("Error: Una o ambas ciudades no existen en el grafo.")
            return False
        
        if not self.graph.has_edge(from_city, to_city):
            print(f"No existe conexión de {from_city} a {to_city}.")
            return False
        
        self.graph.remove_edge(from_city, to_city)
        print(f"Conexión de {from_city} a {to_city} eliminada correctamente.")
        return True
    
    def get_cities(self) -> list:
        """
        Obtiene la lista de ciudades del grafo.
        
        Returns:
            list: Lista de nombres de ciudades
        """
        return sorted(self.graph.nodes())
    
    def get_connections(self) -> list:
        """
        Obtiene la lista de conexiones del grafo.
        
        Returns:
            list: Lista de tuplas (origen, destino, atributos)
        """
        return list(self.graph.edges(data=True))
    
    def get_networkx_graph(self) -> nx.DiGraph:
        """
        Obtiene el grafo de NetworkX subyacente.
        
        Returns:
            nx.DiGraph: El grafo de NetworkX
        """
        return self.graph
