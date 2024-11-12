def convert(binary):
    try:
        int(binary)
    except:
        print('Invalid Input, Must be an Integer.')
    exp = 0
    total = 0
    binary = str(binary)
    for digit in reversed(binary): 
            x = int(digit)*(2**exp)
            total = x + total
            exp +=1
    return total

