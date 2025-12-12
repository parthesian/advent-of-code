with open('input.txt', 'r') as f:
    input_lines = [line.strip() for line in f if line.strip()]

adjacency = {}
memo = {}

adjacency['out'] = []

for line in input_lines:
    device_outputs = line.split(':')
    device = device_outputs[0]
    outputs = device_outputs[1].strip().split(' ')
    adjacency[device] = outputs

def count(node, dest):
    if (node, dest) in memo:
        return memo[(node, dest)]
    
    result = node == dest or sum(count(next, dest) for next in adjacency[node])
    memo[(node, dest)] = result
    return result

valid_paths = count('svr', 'dac') * count('dac', 'fft') * count('fft', 'out') + count('svr', 'fft') * count('fft', 'dac') * count('dac', 'out')

print(valid_paths)