with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f if line.strip()]

def largest_k_digit_number(bank, k):
    n = len(bank)
    result = []
    start = 0
    
    for i in range(k):

        max_voltage = -1
        max_idx = start
        
        for j in range(start, n - (k - i) + 1):
            if bank[j] > max_voltage:
                max_voltage = bank[j]
                max_idx = j
        
        result.append(max_voltage)
        start = max_idx + 1
    
    return result

total_voltage = 0

for str_bank in input_data:
    bank = [int(char) for char in str_bank]
    bank_voltage_list = largest_k_digit_number(bank, 12)
    
    bank_voltage = int(''.join(map(str, bank_voltage_list)))
    print(bank_voltage)
    total_voltage += bank_voltage

print(total_voltage)
    

    


    
