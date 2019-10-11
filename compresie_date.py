with open('compresie_date.txt', 'r') as f:
    size = f.readline()
    data = [x.strip() for x in f.readlines()]

content = [str(x).split(',') for x in data]

for index, elem in enumerate(content):
    content[index] = [int(i) for i in elem]

final = [[] for x in range(int(size))]
temp = 0
count = 0
prev = 0
for ind1, line in enumerate(content):
    for ind, x in enumerate(line):
        if(x is not 0):
            if(count is 0):
                # prima cifra
                temp = x
            if(count > 0):
                # cifra non zero dupa o secventa de zerouri
                final[ind1].append(f'({temp},{count})')
                count = 0
                temp = x
        if(x is 0):
            count = count + 1
        if(prev is not 0 and x is not 0):
            final[ind1].append(str(prev))
        if(ind == len(line)-1):
            final[ind1].append(str(x))
        prev = x
    # print(final[ind1])
    prev = 0

for line in final:
    print(','.join(line))