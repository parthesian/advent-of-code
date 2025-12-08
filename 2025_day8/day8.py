import heapq
from collections import defaultdict, deque

with open('input.txt', 'r') as f:
    junction_box_coordinates = [list(map(int, line.strip().split(","))) for line in f if line.strip()]

connect_count = 1000
top_circuits = 3

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

all_edges = []
for i in range(len(junction_box_coordinates)):
    for j in range(i + 1, len(junction_box_coordinates)):
        dist = distance(junction_box_coordinates[i], junction_box_coordinates[j])
        
        if len(all_edges) < connect_count:
            heapq.heappush(all_edges, (-dist, i, j)) 
        elif dist < -all_edges[0][0]:
            heapq.heapreplace(all_edges, (-dist, i, j))

closest_edges = [(-dist, i, j) for dist, i, j in all_edges]
closest_edges.sort()

adjacency = defaultdict(list)
for dist, i, j in closest_edges:
    adjacency[i].append(j)
    adjacency[j].append(i)

circuits = []

def bfs(start, visited):
    circuit = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        circuit.append(node)
        
        for neighbor in adjacency[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return circuit

visited = set()
for node in adjacency:
    if node not in visited:
        circuit = bfs(node, visited)
        circuits.append(circuit)

circuits.sort(key=len, reverse=True)

res = 1
for circuit in circuits[:top_circuits]:
    res *= len(circuit)
print(res)