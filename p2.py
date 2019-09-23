import sys

breakFlag = 0

cifra1 = [0, 1, 1, 0, 0, 0, 0]
cifra2 = [1, 1, 0, 1, 1, 0, 1]
cifra3 = [1, 1, 1, 1, 0, 0, 1]
cifra4 = [0, 1, 1, 0, 0, 1, 1]
cifra5 = [1, 0, 1, 1, 0, 1, 1]
cifra6 = [1, 0, 1, 1, 1, 1, 1]
cifra7 = [1, 1, 1, 0, 0, 0, 0]
cifra8 = [1, 1, 1, 1, 1, 1, 1]
cifra9 = [1, 1, 1, 1, 0, 1, 1]
cifra0 = [1, 1, 1, 1, 1, 1, 0]

cifre = [
    [cifra1, 1],
    [cifra2, 2],
    [cifra3, 3],
    [cifra4, 4],
    [cifra5, 5],
    [cifra6, 6],
    [cifra7, 7],
    [cifra8, 8],
    [cifra9, 9],
    [cifra0, 0]
]

result = ''
foundDigit = False

with open('p2input.txt', 'r') as f:
    lines = f.readlines()
    
for line in lines:
    digit = [int(x) for x in line.split(',')]
    # digit[-1] = digit[-1].strip()
    foundDigit = False
    for cifra in cifre:
        if(digit[0:7] == cifra[0]):
            foundDigit = True
            result += str(cifra[1])
            if(digit[-1] == 1):
                result += '.'
    if(foundDigit == False):
        print(result)
        sys.exit()
        
print(result)