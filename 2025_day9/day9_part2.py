import itertools

with open('input.txt', 'r') as f:
    input = [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]
looped_input = input + [input[0]]

def area(x1, x2, y1, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

max_area = 0
for (x1, y1), (x2, y2) in itertools.combinations(input, 2):

    box_x1, box_x2 = min(x1, x2), max(x1, x2)
    box_y1, box_y2 = min(y1, y2), max(y1, y2)

    for (segment_x1, segment_y1), (segment_x2, segment_y2) in itertools.pairwise(looped_input):
        if not (max(segment_x1, segment_x2) <= box_x1 or box_x2 <= min(segment_x1, segment_x2) or
                 max(segment_y1, segment_y2) <= box_y1 or box_y2 <= min(segment_y1, segment_y2) ):
            break
    else:
        max_area = max(max_area, area(box_x1, box_x2, box_y1, box_y2))
print(max_area)