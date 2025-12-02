with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f if line.strip()]

input_text = input_data[0]
id_ranges = input_text.split(',')
bad_ids_sum = 0

for id_range in id_ranges:
    first_id, second_id = map(int, id_range.split('-'))
    
    for num in range(first_id, second_id + 1):
        str_num = str(num)
        length = len(str_num)
        
        if length % 2 != 0:
            continue
        
        mid = length // 2
        if str_num[:mid] == str_num[mid:]:
            bad_ids_sum += num

print(bad_ids_sum)