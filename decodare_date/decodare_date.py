with open('decodare_date.txt', 'r') as f:
    f.readline()
    data = []
    for line in f.readlines():
        data.append([int(x) for x in line.split()])

def switch_positions(x):
    for index, digit in enumerate(x):
        if(index % 2 == 0):
            try:
                x[index], x[index+1] = x[index+1], x[index] # asta schimba definitiv (in memorie) variabila data drept parametru
            except:
                break
    # print(x)
    return x

def second_encoding(x):
    for index, digit in enumerate(x):
        # print(index)
        if(index == 0):
            continue
        x[index] = x[index] % 2
    return x

max = 0
sum = 0

for ind, nr in enumerate(data):
    switch_positions(nr)
    second_encoding(nr)
    for digit in nr:
        sum = sum + digit
    if(sum > max):
        max = sum
    sum = 0

print(max)