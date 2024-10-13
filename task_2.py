import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

routes = [
    ('A', 'D'), ('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H'),
    ('E', 'I'), ('F', 'J'), ('G', 'A'), ('H', 'B'), ('I', 'C'),
    ('J', 'D'), ('B', 'E'), ('F', 'H'), ('G', 'I'), ('H', 'J')
]

G.add_nodes_from(stations)
G.add_edges_from(routes)

def dfs(graph, start, goal):
    stack = deque([(start, [start])])
    visited = set()
    edges_count = 0
    
    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path, edges_count
            for neighbor in sorted(set(graph[node]) - visited):
                stack.append((neighbor, path + [neighbor]))
                edges_count += 1
    return None, edges_count

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    edges_count = 0
    
    while queue:
        (node, path) = queue.popleft()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path, edges_count
            for neighbor in sorted(set(graph[node]) - visited):
                queue.append((neighbor, path + [neighbor]))
                edges_count += 1
    return None, edges_count


start = 'G'
goal = 'F'
dfs_path, dfs_edges = dfs(G, start, goal)
print(f"DFS Path from {start} to {goal}: {dfs_path}")
print(f"DFS Edges traversed: {dfs_edges}")

bfs_path, bfs_edges = bfs(G, start, goal)
print(f"BFS Path from {start} to {goal}: {bfs_path}")
print(f"BFS Edges traversed: {bfs_edges}")

colors = ['lightblue', 'orange', 'lightgreen', 'red', 'purple', 'yellow', 'pink', 'gray', 'green', 'brown']
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color=colors, node_size=2000, edge_color='gray', font_size=15)
plt.show()