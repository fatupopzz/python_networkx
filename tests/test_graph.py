"""
Pruebas unitarias para el grafo de logística.
"""

import pytest
import os
import tempfile
from logistica_nx.graph import LogisticaGraph
from logistica_nx.algorithms import shortest_path, find_center


class TestLogisticaGraph:
    """Pruebas para la clase LogisticaGraph."""
    
    @pytest.fixture
    def sample_graph(self):
        """Crea un grafo de ejemplo para las pruebas."""
        graph = LogisticaGraph()
        
        # Crear un archivo temporal con datos de prueba
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
            temp.write("A B 5 8 10 15\n")
            temp.write("B C 3 4 6 9\n")
            temp.write("C D 2 3 5 8\n")
            temp.write("A D 15 20 25 30\n")
            temp_name = temp.name
        
        # Cargar el grafo desde el archivo temporal
        graph.load_from_file(temp_name)
        
        # Limpiar archivo temporal
        os.unlink(temp_name)
        
        return graph
    
    def test_load_from_file(self, sample_graph):
        """Prueba la carga del grafo desde un archivo."""
        # Verificar que el grafo se cargó correctamente
        assert len(sample_graph.get_cities()) == 4
        assert len(sample_graph.get_connections()) == 4
    
    def test_set_weather(self, sample_graph):
        """Prueba el cambio de clima."""
        # Cambiar a clima de lluvia
        sample_graph.set_weather("rain")
        assert sample_graph.current_weather == "rain"
        
        # Verificar que los pesos se actualizaron
        g = sample_graph.get_networkx_graph()
        assert g["A"]["B"]["weight"] == 8.0
    
    def test_add_connection(self, sample_graph):
        """Prueba la adición de conexiones."""
        times = {'normal': 7, 'rain': 10, 'snow': 12, 'storm': 18}
        sample_graph.add_connection("D", "B", times)
        
        g = sample_graph.get_networkx_graph()
        assert g.has_edge("D", "B")
        assert g["D"]["B"]["normal"] == 7
    
    def test_remove_connection(self, sample_graph):
        """Prueba la eliminación de conexiones."""
        sample_graph.remove_connection("A", "B")
        
        g = sample_graph.get_networkx_graph()
        assert not g.has_edge("A", "B")
    
    def test_shortest_path(self, sample_graph):
        """Prueba la búsqueda de la ruta más corta."""
        g = sample_graph.get_networkx_graph()
        path, distance = shortest_path(g, "A", "D")
        
        # La ruta A -> B -> C -> D es más corta que A -> D directamente
        assert path == ["A", "B", "C", "D"]
        assert distance == 10.0  # 5 + 3 + 2
    
    def test_graph_center(self, sample_graph):
        """Prueba el cálculo del centro del grafo."""
        g = sample_graph.get_networkx_graph()
        center = find_center(g)
        
        # El centro dependerá de la estructura del grafo
        assert center in ["A", "B", "C", "D"]


if __name__ == "__main__":
    pytest.main()
