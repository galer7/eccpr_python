

def semnulExclamarii(n):
    result = 1
    while(n > 0):
        result = result*n
        n = n - 1
    return result

def aranjamente(n, k):
    result = semnulExclamarii(n) / semnulExclamarii(n-k)
    return int(result)

with open('aranj_produse.txt', 'r') as f:
    x = f.readline()

[k, M] = [int(readResult) for readResult in x.split()]

start = k
result = 0

while(1):
    # print(start)
    # print(aranjamente(start, k))
    if(k < 0):
        result = 0
        break
    if(aranjamente(start, k) > M):
        break
    else: # mai mic
        result = start
        start = start + 1

print(result)
