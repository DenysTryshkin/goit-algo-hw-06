import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()
cities = ["Париж", "Берлін", "Мадрид", "Рим", "Амстердам", "Відень"]
G.add_nodes_from(cities)

# Додавання ребер між містами
edges = [
    ("Париж", "Берлін"),
    ("Париж", "Амстердам"),
    ("Берлін", "Відень"),
    ("Мадрид", "Рим"),
    ("Рим", "Берлін"),
    ("Відень", "Мадрид"),
    ("Рим", "Амстердам"),
]

G.add_edges_from(edges)
pos = nx.circular_layout(G)

edge_labels = {
    ("Париж", "Берлін"): "1",
    ("Париж", "Амстердам"): "2",
    ("Берлін", "Відень"): "3",
    ("Мадрид", "Рим"): "4",
    ("Рим", "Берлін"): "5",
    ("Відень", "Мадрид"): "6",
    ("Рим", "Амстердам"): "7",
}

# Відображення графа
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2000,
    edge_color="blue",
    font_size=15,
    font_color="darkgreen",
)

# Відображення міток ребер
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="red",
    font_size=12,
)

# Відображення графа
plt.title("Транспортна мережа міст Європи")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")
