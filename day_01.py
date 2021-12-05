from helper import input_to_list

input = input_to_list('day_01_input.txt')

def count_larger_than_prev(numbers: [str]) -> int:
    
    count = 0
    
    for i in range(1, len(numbers)):
        if int(numbers[i-1]) < int(numbers[i]):
            count += 1
    
    return count

def count_three_sum_larger_than_prev(numbers: [str], size: int) -> int:
    
    count = 0
    curr_sum = 0
    
    for i in range(size):
        curr_sum += int(numbers[i])
    
    for i in range(size, len(numbers)):
        prev_sum = curr_sum
        curr_sum = prev_sum - int(numbers[i-3]) + int(numbers[i])
        
        if prev_sum < curr_sum:
            count += 1
    
    return count

print(f'First part of answer is {count_larger_than_prev(input)}.')
print(f'Second part of answer is {count_three_sum_larger_than_prev(input, 3)}.')