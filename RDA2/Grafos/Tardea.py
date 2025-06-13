# Importamos las librerías necesarias para trabajar con grafos y visualización
import networkx as nx
import matplotlib.pyplot as plt

# 1. Creamos un grafo dirigido y ponderado
# Un grafo dirigido permite que las rutas tengan dirección (por ejemplo, ir de Quito a Cuenca no es lo mismo que al revés)
grafo_transporte = nx.DiGraph()

# Agregamos las ciudades que representarán los nodos del grafo
ciudades = ['Quito', 'Ambato', 'Riobamba', 'Cuenca']
grafo_transporte.add_nodes_from(ciudades)

# Definimos las rutas entre las ciudades, junto con su costo (representado como peso del grafo)
rutas = [
    ('Quito', 'Ambato', 10),       # De Quito a Ambato, costo 10
    ('Quito', 'Riobamba', 18),     # De Quito a Riobamba, costo 18
    ('Ambato', 'Cuenca', 25),      # De Ambato a Cuenca, costo 25
    ('Riobamba', 'Cuenca', 20)     # De Riobamba a Cuenca, costo 20
]
# Agregamos las rutas con sus respectivos pesos al grafo
grafo_transporte.add_weighted_edges_from(rutas)

# 2. Visualizamos el grafo
# Calculamos una disposición automática de los nodos para una mejor presentación
pos = nx.spring_layout(grafo_transporte)

# Dibujamos el grafo con sus nodos, aristas y estilo personalizado
nx.draw(
    grafo_transporte,
    pos,
    with_labels=True,
    node_size=2000,
    node_color='lightblue',
    font_size=10,
    font_weight='bold'
)

# Mostramos los pesos (costos) en cada conexión
labels = nx.get_edge_attributes(grafo_transporte, 'weight')
nx.draw_networkx_edge_labels(grafo_transporte, pos, edge_labels=labels)

# Añadimos un título a la visualización
plt.title('Rutas entre ciudades con costos (pesos del grafo)')
plt.show()

# 3. Determinamos el camino con menor costo desde Quito hasta Cuenca
# Utilizamos el algoritmo de Dijkstra para encontrar la ruta óptima
camino_mas_barato = nx.dijkstra_path(grafo_transporte, 'Quito', 'Cuenca')
costo_total = nx.dijkstra_path_length(grafo_transporte, 'Quito', 'Cuenca')

# Imprimimos el resultado de manera clara
print(f"\nCamino con menor costo de Quito a Cuenca: {camino_mas_barato}")
print(f"Costo total del camino (peso acumulado): {costo_total}")
