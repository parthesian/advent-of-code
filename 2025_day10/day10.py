import numpy as np
from collections import deque

with open('input.txt', 'r') as f:
    input = [line.strip() for line in f if line.strip()]

def light_diagram_to_binary(light_diagram):

    return np.array([1 if char == '#' else 0 for char in light_diagram if char in '.#'], dtype=np.uint8)

def button_to_binary(button, num_lights):

    binary = [0] * num_lights
    numbers = button.strip('()').split(',')
    for num_str in numbers:
        if num_str.strip():
            index = int(num_str.strip())
            binary[index] = 1
    return np.array(binary, dtype=np.uint8)

def buttons_to_binary(buttons, num_lights):

    result = []
    for button in buttons:
        result.append(button_to_binary(button, num_lights))
    return np.array(result, dtype=np.uint8)

def min_button_presses(initial_state, goal_state, buttons):

    initial_tuple = tuple(initial_state)
    goal_tuple = tuple(goal_state)
    
    if initial_tuple == goal_tuple:
        return 0

    visited = {initial_tuple: 0}
    queue = deque([initial_tuple])
    
    while queue:
        current_state = queue.popleft()
        current_presses = visited[current_state]
        
        for button in buttons:

            new_state = tuple(np.array(current_state) ^ button)
            
            if new_state == goal_tuple:
                return current_presses + 1
            
            if new_state not in visited:
                visited[new_state] = current_presses + 1
                queue.append(new_state)
    
    return -1

total_presses = 0

for line in input:
    last_square_bracket_idx = line.index(']')
    first_curly_bracket_idx = line.index('{')

    goal_state = light_diagram_to_binary(line[:last_square_bracket_idx + 1].strip())
    num_lights = len(goal_state)
    initial_state = light_diagram_to_binary('.' * num_lights)

    buttons_list = line[last_square_bracket_idx + 1:first_curly_bracket_idx].strip().split(' ')
    buttons = buttons_to_binary(buttons_list, num_lights)

    min_presses = min_button_presses(initial_state, goal_state, buttons)
    total_presses += min_presses

print(total_presses)