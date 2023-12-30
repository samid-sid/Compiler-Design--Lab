def leftmost_derivation(input_str):
    derivation = "aAB"
    print("Leftmost Derivation:")
    
    for i in range(len(input_str)):
        if derivation[i] == 'A':
            if input_str[i] == 'b':
                derivation = derivation[:i] + 'b' + derivation[i+1:]
            else:
                derivation = derivation[:i] + 'ε' + derivation[i+1:]
        elif derivation[i] == 'B':
            if input_str[i] == 'c':
                derivation = derivation[:i] + 'c' + derivation[i+1:]
            else:
                derivation = derivation[:i] + 'ε' + derivation[i+1:]
        
    print(f"Step {1}: {derivation}")

    print("\n")

def rightmost_derivation(input_str):
    derivation = "aAB"
    print("Rightmost Derivation:")
    
    for i in range(len(input_str) - 1, -1, -1):
        if derivation[i] == 'A':
            if input_str[i] == 'b':
                derivation = derivation[:i] + 'b' + derivation[i+1:]
            else:
                derivation = derivation[:i] + 'ε' + derivation[i+1:]
        elif derivation[i] == 'B':
            if input_str[i] == 'c':
                derivation = derivation[:i] + 'c' + derivation[i+1:]
            else:
                derivation = derivation[:i] + 'ε' + derivation[i+1:]
        
    print(f"Step {1}: {derivation}")

    print("\n")

# Main Function
if __name__ == '__main__':
    input_str = "abc"
    leftmost_derivation(input_str)
    rightmost_derivation(input_str)
