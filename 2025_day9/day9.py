import itertools

with open('input.txt', 'r') as f:
    input = [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]
looped_input = input + [input[0]]

def area(x1, x2, y1, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

max_area = max(area(x1, x2, y1, y2)
            for (x1, y1), (x2, y2) in itertools.combinations(input, 2))
print(max_area)
