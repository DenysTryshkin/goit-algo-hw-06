import networkx as nx

G = nx.Graph()
cities = ["Париж", "Берлін", "Мадрид", "Рим", "Амстердам", "Відень"]
G.add_nodes_from(cities)

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

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(reversed(list(graph.neighbors(vertex))))  
    return path        

def bfs_iterative(graph, start):
    visited = set()
    queue = ([start])
    path =[]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return path

start_city = "Париж"
dfs_path = dfs_iterative(G, start_city)
bfs_path = bfs_iterative(G, start_city)

print("DFS:", dfs_path)
print("BFS:", bfs_path)