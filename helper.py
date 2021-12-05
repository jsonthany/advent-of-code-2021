def input_to_list(path) -> list():
    
    output = []
    
    with open(path) as file:
        for line in file:
            output.append(line.strip())
            
    return output