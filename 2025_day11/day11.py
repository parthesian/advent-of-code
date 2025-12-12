with open('input.txt', 'r') as f:
    input_lines = [line.strip() for line in f if line.strip()]

adjacency = {}

for line in input_lines:
    device_outputs = line.split(':')
    device = device_outputs[0]
    outputs = device_outputs[1].strip().split(' ')
    adjacency[device] = outputs

def dfs(node):
    if node == "out":
        return 1
    
    paths = 0
    for other_node in adjacency[node]:
        paths += dfs(other_node)
    return paths

total_paths = dfs("you")

print(total_paths)