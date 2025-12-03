with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f if line.strip()]

total_voltage = 0

for str_bank in input_data:
    bank = [int(char) for char in str_bank]

    max_idx = -1
    max_voltage = float('-inf')
    
    for i, voltage in enumerate(bank):
        if voltage > max_voltage:
            max_idx = i
            max_voltage = voltage
        
    if max_idx == len(bank) - 1:
        left_max_voltage = max(bank[:max_idx])
        total_voltage += 10 * left_max_voltage + max_voltage
    else:
        right_max_voltage = max(bank[max_idx + 1:])
        total_voltage += 10 * max_voltage + right_max_voltage

print(total_voltage)
    

    


    
