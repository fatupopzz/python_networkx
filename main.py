"""
Programa principal para el Sistema de Logística con NetworkX.
"""

from logistica_nx.graph import LogisticaGraph
from logistica_nx.algorithms import shortest_path, find_center, get_adjacency_matrix
from logistica_nx.utils import visualize_graph, print_adjacency_matrix, validate_menu_option, validate_float_input


def main():
    """Función principal del programa."""
    print("\n=== Sistema de Logística - Grafos y Algoritmo de Floyd (NetworkX) ===\n")
    
    # Crear el grafo
    logistica = LogisticaGraph()
    
    # Cargar el grafo desde el archivo
    filename = input("Ingrese el nombre del archivo (por defecto: logistica.txt): ").strip()
    if not filename:
        filename = "data/logistica.txt"
    
    print(f"\nCargando datos desde {filename}...")
    if not logistica.load_from_file(filename):
        print("No se pudo cargar el grafo. Finalizando programa.")
        return
    
    # Variable para controlar el bucle principal
    running = True
    
    # Menú principal
    while running:
        print("\n=== Menú Principal ===")
        print("1. Consultar ruta más corta entre ciudades")
        print("2. Mostrar centro del grafo")
        print("3. Modificar el grafo")
        print("4. Mostrar matriz de adyacencia")
        print(f"5. Cambiar condición climática (Actual: {logistica.current_weather})")
        print("6. Visualizar grafo")
        print("7. Salir")
        
        option = validate_menu_option("\nSeleccione una opción: ", 1, 7)
        
        if option == 1:
            # Consultar ruta más corta
            handle_shortest_path(logistica)
        
        elif option == 2:
            # Mostrar centro del grafo
            handle_graph_center(logistica)
        
        elif option == 3:
            # Modificar el grafo
            handle_modify_graph(logistica)
        
        elif option == 4:
            # Mostrar matriz de adyacencia
            handle_adjacency_matrix(logistica)
        
        elif option == 5:
            # Cambiar condición climática
            handle_change_weather(logistica)
        
        elif option == 6:
            # Visualizar grafo
            visualize_graph(logistica.get_networkx_graph(), 
                           title=f"Grafo de Logística (Clima: {logistica.current_weather})")
        
        elif option == 7:
            # Salir
            running = False
            print("\n¡Gracias por usar el Sistema de Logística!")


def handle_shortest_path(logistica: LogisticaGraph) -> None:
    """Maneja la consulta de rutas más cortas."""
    print(f"\n=== Consulta de Ruta Más Corta ({logistica.current_weather}) ===")
    
    # Mostrar ciudades disponibles
    cities = logistica.get_cities()
    print("\nCiudades disponibles:")
    for i, city in enumerate(cities):
        print(f"{i+1}. {city}")
    
    # Seleccionar ciudades
    origin = input("\nIngrese el nombre de la ciudad origen: ")
    destination = input("Ingrese el nombre de la ciudad destino: ")
    
    # Encontrar la ruta más corta
    path, distance = shortest_path(logistica.get_networkx_graph(), origin, destination)
    
    if path and distance is not None:
        print("\n=== Ruta encontrada ===")
        print("Ruta más corta:", " -> ".join(path))
        print(f"Tiempo total: {distance:.2f} horas")
        
        # Preguntar si desea visualizar la ruta
        if input("\n¿Desea visualizar la ruta? (s/n): ").lower() == 's':
            visualize_graph(logistica.get_networkx_graph(), path, 
                          f"Ruta {origin} a {destination} ({logistica.current_weather})")


def handle_graph_center(logistica: LogisticaGraph) -> None:
    """Maneja la consulta del centro del grafo."""
    print("\n=== Centro del Grafo ===")
    center = find_center(logistica.get_networkx_graph())
    if center:
        print("El centro del grafo es:", center)
        print("(Ciudad con la menor excentricidad)")
    else:
        print("No se pudo calcular el centro del grafo.")


def handle_adjacency_matrix(logistica: LogisticaGraph) -> None:
    """Maneja la visualización de la matriz de adyacencia."""
    adj_matrix, nodes = get_adjacency_matrix(logistica.get_networkx_graph())
    print_adjacency_matrix(adj_matrix, nodes)


def handle_change_weather(logistica: LogisticaGraph) -> None:
    """Maneja el cambio de condición climática."""
    print("\n=== Cambiar Condición Climática ===")
    print("1. Normal")
    print("2. Lluvia")
    print("3. Nieve")
    print("4. Tormenta")
    
    option = validate_menu_option("\nSeleccione el clima (ingrese el número): ", 1, 4)
    
    weather_types = {1: "normal", 2: "rain", 3: "snow", 4: "storm"}
    logistica.set_weather(weather_types[option])


def handle_modify_graph(logistica: LogisticaGraph) -> None:
    """Maneja la modificación del grafo."""
    print("\n=== Modificar Grafo ===")
    print("1. Interrupción de tráfico entre ciudades")
    print("2. Establecer nueva conexión entre ciudades")
    
    option = validate_menu_option("\nSeleccione una opción: ", 1, 2)
    
    # Mostrar ciudades disponibles
    cities = logistica.get_cities()
    print("\nCiudades disponibles:")
    for i, city in enumerate(cities):
        print(f"{i+1}. {city}")
    
    if option == 1:
        # Interrupción de tráfico
        from_city = input("\nIngrese el nombre de la ciudad origen: ")
        to_city = input("Ingrese el nombre de la ciudad destino: ")
        logistica.remove_connection(from_city, to_city)
    
    elif option == 2:
        # Nueva conexión
        from_city = input("\nIngrese el nombre de la ciudad origen: ")
        to_city = input("Ingrese el nombre de la ciudad destino: ")
        
        times = {
            'normal': validate_float_input("Tiempo normal (horas): "),
            'rain': validate_float_input("Tiempo con lluvia (horas): "),
            'snow': validate_float_input("Tiempo con nieve (horas): "),
            'storm': validate_float_input("Tiempo con tormenta (horas): ")
        }
        
        logistica.add_connection(from_city, to_city, times)


if __name__ == "__main__":
    main()
