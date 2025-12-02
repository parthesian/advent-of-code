with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f if line.strip()]

input_text = input_data[0]
id_ranges = input_text.split(',')
bad_ids_sum = 0

factors_map = {}

def factors(n):
    if n in factors_map:
        return factors_map[n]
    
    factor_set = set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )
    factor_set.discard(1)  # Remove 1 if present
    factors_map[n] = factor_set
    return factor_set

for id_range in id_ranges:
    first_id, second_id = map(int, id_range.split('-'))
    
    for num in range(first_id, second_id + 1):
        str_num = str(num)
        length = len(str_num)

        factors_of_length = factors(length)

        for factor in factors_of_length:
            distance = length // factor
            first_interval = str_num[0:distance]
            
            for i in range(factor):
                this_interval = str_num[distance * i:distance*(i+1)]
                if this_interval != first_interval:
                    break
            else:
                bad_ids_sum += num
                break

print(bad_ids_sum)