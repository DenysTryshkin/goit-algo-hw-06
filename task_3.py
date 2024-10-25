import networkx as nx

G = nx.Graph()
cities = ["Париж", "Берлін", "Мадрид", "Рим", "Амстердам", "Відень"]
G.add_nodes_from(cities)

# Додавання ребер з вагами
edges_with_weights = [
    ("Париж", "Берлін", 5),
    ("Париж", "Амстердам", 3),
    ("Берлін", "Відень", 2),
    ("Мадрид", "Рим", 4),
    ("Рим", "Берлін", 1),
    ("Відень", "Мадрид", 6),
    ("Рим", "Амстердам", 7),
]

G.add_weighted_edges_from(edges_with_weights)

def dijkstra_all_pairs(graph):
    # Зберігаємо найкоротші шляхи для всіх пар вершин
    shortest_paths = {}
    for city in graph.nodes:
        # Використовуємо алгоритм Дейкстри для кожної вершини
        shortest_paths[city] = nx.single_source_dijkstra_path(graph, city)
    return shortest_paths

# Виклик функції для знаходження найкоротких шляхів між усіма вершинами
all_shortest_paths = dijkstra_all_pairs(G)

# Виведення результатів
for start_city, paths in all_shortest_paths.items():
    print("********")
    print(f"Найкоротші шляхи від {start_city}:")
    for end_city, path in paths.items():
        distance = nx.path_weight(G, path, weight='weight')
        print(f"До {end_city}: шлях {path}, відстань {distance}")