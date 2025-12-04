import copy
with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f if line.strip()]

diagram = []

for line in input_data:
    new_line = []
    for char in line:
        new_line.append(char)
    diagram.append(new_line)

directions = [
    [-1,-1],
    [-1, 0],
    [-1, 1],
    [1,-1],
    [1, 0],
    [1, 1],
    [0,-1],
    [0, 1],
    ]

def scan(i, j):
    filled_adjacent = 0
    if diagram[i][j] == '@':
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if new_i >= 0 and new_i < len(diagram) and new_j >= 0 and new_j < len(diagram[0]) and diagram[new_i][new_j] == '@':
                filled_adjacent += 1
        if filled_adjacent < 4:
            return True
    return False
    
new_diagram = copy.deepcopy(diagram)
num_xs = 0

for i in range(len(diagram)):
    for j in range(len(diagram[0])):
        if scan(i, j):
            new_diagram[i][j] = 'X'
            num_xs += 1

for line in new_diagram:
    print(''.join(map(str, line)))

print(num_xs)