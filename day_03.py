from helper import input_to_list

input = input_to_list('day_03_input.txt')

def get_epsilon_gamma_multiple(input) -> int:
    
    bin_pos_count_ls = [0]*len(input[0])
    
    for bin in input:
        for i in range(len(bin)):
            if bin[i] == "1":
                bin_pos_count_ls[i] += 1
            else:
                bin_pos_count_ls[i] -= 1
    
    gamma   = ""
    epsilon = ""
    
    for count in bin_pos_count_ls:
        if count > 0:
            gamma += "1"
            epsilon += "0"
        elif count < 0:
            gamma += "0"
            epsilon += "1"
    
    return int(gamma, 2) * int(epsilon, 2)

def get_CO2_rating(input, idx):
    
    if len(input) == 1:
        return int(input[0], 2)
    
    new_inputs = dict()
    
    for bin in input:
        if bin[idx] not in new_inputs:
            new_inputs[bin[idx]] = [bin]
        else:
            new_inputs[bin[idx]].append(bin)
    
    if len(new_inputs["0"]) <= len(new_inputs["1"]):
        return get_CO2_rating(new_inputs["0"], idx + 1)
    else:
        return get_CO2_rating(new_inputs["1"], idx + 1)

def get_O2_rating(input, idx):
    
    if len(input) == 1:
        return int(input[0], 2)
    
    new_inputs = dict()
    
    for bin in input:
        if bin[idx] not in new_inputs:
            new_inputs[bin[idx]] = [bin]
        else:
            new_inputs[bin[idx]].append(bin)
    
    if len(new_inputs["1"]) >= len(new_inputs["0"]):
        return get_O2_rating(new_inputs["1"], idx + 1)
    else:
        return get_O2_rating(new_inputs["0"], idx + 1)


def get_life_support_rating(input):
    
    return get_CO2_rating(input, 0) * get_O2_rating(input, 0)

input_example = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

print(f'First part of answer is {get_epsilon_gamma_multiple(input)}.')
print(f'Second part of answer is {get_life_support_rating(input)}.')