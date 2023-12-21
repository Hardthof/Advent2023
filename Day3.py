import numpy as np 

def hasAdjacentSymbol(symbols, candidate, xlim, ylim):
    # print(symbols)
    print(candidate)

    n = set()
    for i in range(len(candidate)):
        if i == 0:
            # right
            if candidate[0] +1 < xlim: n.add((candidate[0] + 1, candidate[1]))
        if i == len(candidate) -1:
            if candidate[0] > 0: n.add((candidate[0] - 1, candidate[1]))
        
        if candidate[1] +1 < ylim: n.add((candidate[0], candidate[1] + 1))
        if candidate[1] > 0: n.add((candidate[0], candidate[1] - 1))

    return any(entry in symbols for entry in candidate)


if __name__ == '__main__':

    matrix = []
    with open('Day3.txt', 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row) 

    symbols = set()
    numberCandidates = set()

    for x,line in enumerate(matrix):
        number = ''
        for y,c in enumerate(line):
            if c.isdigit(): 
                number += c    
            elif c == '.': 
                if number:
                    numberCandidates.add((x,y, number))
                    number = ''
            else:
                symbols.add((x,y))
    
    for candidate in numberCandidates:
        print(hasAdjacentSymbol(symbols, candidate, len(matrix), len(matrix[0])))
    