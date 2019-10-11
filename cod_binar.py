import math

with open('cod_binar.txt', 'r') as f:
    f.readline() # nr de linii care urmeaza
    numbers = [int(x) for x in f.readlines()]

def binar(x):
    counter = 0
    number = str(bin(x))[2:]
    while(len(number) < 8):
        number = number + '0'
    # print(number)
    for digit in number:
        if(digit is '0'):
            counter = counter + 1
    return counter

# print(numbers)
max = 0
for number in numbers:
    if(binar(number) > max):
        max = binar(number)

for number in numbers:
    if(binar(number) == max):
        print(number)