import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

routes_with_weights  = [
    ('A', 'D', 1), ('A', 'E', 2), ('B', 'F', 3), ('C', 'G', 2), ('D', 'H', 3),
    ('E', 'I', 2.5), ('F', 'J', 2.5), ('G', 'A', 1.5), ('H', 'B', 1), ('I', 'C', 2),
    ('J', 'D', 1.5), ('B', 'E', 3), ('F', 'H', 2), ('G', 'I', 2), ('H', 'J', 1.5)
]

G.add_nodes_from(stations)
G.add_weighted_edges_from(routes_with_weights)

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)
    
    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        if distances[current_node] == float('inf'):
            break

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_node)

    return distances

shortest_paths_from_A = dijkstra(G, 'A')

print("Найкоротші шляхи від вузла 'A' до всіх інших вершин:")
for target, length in shortest_paths_from_A.items():
    print(f"Від 'A' до '{target}' = {length} одиниць")

def all_pairs_shortest_paths(graph):
    all_paths = {}
    for node in graph.nodes:
        all_paths[node] = dijkstra(graph, node)
    return all_paths

all_shortest_paths = all_pairs_shortest_paths(G)

print("\nНайкоротші шляхи між усіма вершинами:")
for source, paths in all_shortest_paths.items():
    print(f"\nВершина '{source}':")
    for target, length in paths.items():
        print(f"  до '{target}' = {length} одиниць")

pos = nx.spring_layout(G)
weights = nx.get_edge_attributes(G, 'weight')
colors = ['lightblue', 'orange', 'lightgreen', 'red', 'purple', 'yellow', 'pink', 'gray', 'green', 'brown']
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000, edge_color='gray', font_size=15)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
plt.show()