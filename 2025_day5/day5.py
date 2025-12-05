with open('input.txt', 'r') as f:
    intervals, ingredients = [], []
    for line in (l.strip() for l in f if l.strip()):
        (intervals if '-' in line else ingredients).append(tuple(map(int, line.split('-'))) if '-' in line else int(line))


fresh = 0

for ingredient in ingredients:
    for interval in intervals:
        if ingredient >= interval[0] and ingredient <= interval[1]:
            fresh += 1
            break

print(fresh)