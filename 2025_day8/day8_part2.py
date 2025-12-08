import heapq
from collections import defaultdict, deque

with open('input.txt', 'r') as f:
    junction_box_coordinates = [list(map(int, line.strip().split(","))) for line in f if line.strip()]

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

all_edges = []
for i in range(len(junction_box_coordinates)):
    for j in range(i + 1, len(junction_box_coordinates)):
        dist = distance(junction_box_coordinates[i], junction_box_coordinates[j])
        heapq.heappush(all_edges, (dist, i, j))

def bfs(start, adjacency, visited):
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

res = -1
adjacency = defaultdict(list)

while all_edges:
    dist, i, j = heapq.heappop(all_edges)
    
    adjacency[i].append(j)
    adjacency[j].append(i)
    
    visited = set()
    circuits = []
    
    for node in adjacency:
        if node not in visited:
            circuit = bfs(node, adjacency, visited)
            circuits.append(circuit)
    
    if len(circuits) == 1 and len(circuits[0]) == len(junction_box_coordinates):
        res = junction_box_coordinates[i][0] * junction_box_coordinates[j][0]
        break

print(res)