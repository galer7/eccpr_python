def delay(x, nr):
    tmp = x
    while(nr > 0):
        tmp.insert(0, 0)
        tmp.pop()
        nr = nr - 1
    return tmp

with open('intarziere_semnal.txt', 'r') as f:
    n = int(f.readline())
    semnale = [x.strip() for x in f.readlines()]
    for index, semnal in enumerate(semnale):
        semnale[index] = [int(x) for x in semnal.split()]

delta = [1, 2]

result = [[] for x in range(n+1)]
for x in zip(*semnale):
    tmp = sum(list(x))/n
    result[0].append(tmp)

for nr in delta:
    for ind, semnal in enumerate(semnale):
        semnale[ind] = delay(semnal, ind)

    for x in zip(*semnale):
        tmp = sum(list(x))/n
        result[nr].append(tmp)

for r in result:
    for elem in r:
        print(f'{elem:.2f}', end=' ')
    print()