from helper import input_to_list

input = input_to_list('day_02_input.txt')

def get_total(directions) -> int:
    
    direction_count = {
        "up": 0,
        "down": 0,
        "forward": 0,
    }
    
    for dir in directions:
        [direction, steps] = dir.split(" ")
        direction_count[direction] += int(steps)
        
    return (direction_count["down"] - direction_count["up"]) * direction_count["forward"]

def get_total_depth_multiple(directions) -> int:
    
    direction_count = {
        "up": 0,
        "down": 0,
        "forward": 0,
    }
    
    depth = 0
    
    for dir in directions:
        [direction, steps] = dir.split(" ")
        direction_count[direction] += int(steps)
        
        if direction == "forward":
            depth += (direction_count["down"] - direction_count["up"]) * int(steps)
        
    return depth * direction_count["forward"]

input2 = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

print(f'First part of answer is {get_total(input)}.')
print(f'Second part of answer is {get_total_depth_multiple(input)}.')
print(f'Second part of answer is {get_total_depth_multiple(input2)}.')