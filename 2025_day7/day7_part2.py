with open('input.txt', 'r') as f:
    tachyon_manifold = [list(line.strip()) for line in f if line.strip()]

start_col = tachyon_manifold[0].index('S')
manifold_length = len(tachyon_manifold)
col_count = len(tachyon_manifold[0])

current_positions = {(0, start_col): 1}
total_exits = 0

while current_positions:

    next_positions = {}
    
    for (row, col), path_count in current_positions.items():

        current_row = row
        
        while current_row < manifold_length and tachyon_manifold[current_row][col] != '^':
            current_row += 1
        
        if current_row >= manifold_length:
            total_exits += path_count

        elif tachyon_manifold[current_row][col] == '^':

            next_row = current_row + 1
            if col > 0:
                next_positions[(next_row, col - 1)] = next_positions.get((next_row, col - 1), 0) + path_count
            if col + 1 < col_count:
                next_positions[(next_row, col + 1)] = next_positions.get((next_row, col + 1), 0) + path_count
    
    current_positions = next_positions

print(total_exits)