import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

edges = [
    (100, 50),
    (100, 150),
    (50, 25),
    (50, 75),
    (150, 125),
    (150, 175)
]

G.add_edges_from(edges)

pos = {
    100: (0, 2),
    50: (-1.5, 1),
    150: (1.5, 1),
    25: (-2.2, 0),
    75: (-0.8, 0),
    125: (0.8, 0),
    175: (2.2, 0)
}

plt.figure(figsize=(10, 6))

nx.draw(
    G, pos,
    with_labels=True,
    node_color='skyblue',
    node_size=1800,
    font_size=14,
    font_weight='bold',
    arrows=False
)

plt.title("Árbol Binario de Búsqueda: [100, 50, 150, 25, 75, 125, 175]", fontsize=16)
plt.axis('off')
plt.show()
