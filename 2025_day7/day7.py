with open('input.txt', 'r') as f:
    tachyon_manifold = [list(line.strip()) for line in f if line.strip()]

start_col = tachyon_manifold[0].index('S')
manifold_length = len(tachyon_manifold)
col_count = len(tachyon_manifold[0])

splitters = set()
queue = [(0, start_col)]

while queue:
    row, col = queue.pop(0)
    
    if row >= manifold_length or tachyon_manifold[row][col] == '|':
        continue
    
    while row < manifold_length and tachyon_manifold[row][col] != '^':
        if tachyon_manifold[row][col] != 'S':
            tachyon_manifold[row][col] = '|'
        row += 1
    
    if row < manifold_length and tachyon_manifold[row][col] == '^':
        if (row, col) in splitters:
            continue
        splitters.add((row, col))
        
        if col + 1 < col_count:
            queue.append((row, col + 1))
        if col > 0:
            queue.append((row, col - 1))

for row in tachyon_manifold:
    print(''.join(row))
print(len(splitters))


