from math import pi

with open('forma_geometrica.txt', 'r') as f:
    f.readline()
    data = []
    for line in f.readlines():
        data.append([x for x in line.strip().split()])

maxArea = 0
tmpIndex = 0
currArea = 0

for index, forma in enumerate(data):
    if(forma[0] == 'cerc'):
        currArea = pi * float(forma[1]) * float(forma[1])
    if(forma[0] == 'patrat'):
        currArea = float(forma[1]) * float(forma[1])
    if(forma[0] == 'dreptunghi'):
        currArea = float(forma[1]) * float(forma[2])
    if(currArea > maxArea):
        maxArea = currArea
        tmpIndex = index

print(f'{data[tmpIndex][0]} {data[tmpIndex][1]}')