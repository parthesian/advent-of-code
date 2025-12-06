with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f if line.strip()]

multiply_buckets = []
add_buckets = []
operators = ['+', '*']
operator_line = input_data[-1]

last_operator = 0
for i, char in enumerate(operator_line):
    if char in operators and i != 0:
        bucket = [int(line[last_operator:i-1].strip()) for line in input_data[:-1]]
        
        if operator_line[last_operator] == '+':
            add_buckets.append(bucket)
        else:
            multiply_buckets.append(bucket)
        
        last_operator = i

bucket = [int(line[last_operator:].strip()) for line in input_data[:-1]]
if operator_line[last_operator] == '+':
    add_buckets.append(bucket)
else:
    multiply_buckets.append(bucket)

total = 0

for bucket in multiply_buckets:
    val = 1
    for item in bucket:
        val *= item
    total += val

for bucket in add_buckets:
    total += sum(bucket)

print(total)