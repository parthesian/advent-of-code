with open('input.txt', 'r') as f:
    inputs = [line.strip() for line in f if line.strip()]

ptr = 50
dial_size = 100

part1_pwd = 0
part2_pwd = 0

for input in inputs:

    last_ptr = ptr

    direction = input[0]
    sign = 1 if direction == 'R' else -1
    amount = int(input[1:])

    spins = amount // dial_size
    part2_pwd += spins

    remainder = amount % dial_size
    ptr += sign * remainder
    ptr = ptr % dial_size

    crossed_zero = (direction == 'L' and ptr > last_ptr) or (direction == 'R' and ptr < last_ptr)
    if crossed_zero and ptr != 0 and last_ptr != 0:
       part2_pwd += 1
    
    if ptr == 0:
        part1_pwd += 1
        part2_pwd += 1

    
print("Part 1 Password:", part1_pwd)
print("Part 2 Password:", part2_pwd)