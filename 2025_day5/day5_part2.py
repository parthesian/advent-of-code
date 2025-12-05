with open('input.txt', 'r') as f:
    intervals, ingredients = [], []
    for line in (l.strip() for l in f if l.strip()):
        (intervals if '-' in line else ingredients).append(tuple(map(int, line.split('-'))) if '-' in line else int(line))

intervals.sort(key=lambda x:x[0])
merged_intervals = []

last_interval = None

for i in range(len(intervals)):
    if last_interval != None:
        if last_interval[1] >= intervals[i][0]:
            intervals[i] = (min(intervals[i][0], last_interval[0]), max(intervals[i][1], last_interval[1]))
        else:
            merged_intervals.append(last_interval)
    last_interval = intervals[i]
merged_intervals.append(last_interval)

fresh = sum(end - start + 1 for start, end in merged_intervals)



print(fresh)