
def semnulExclamarii(n):
    result = 1
    while(n > 0):
        result = result*n
        n = n - 1
    return result

def combinari(n, k):
    result = semnulExclamarii(n) / (semnulExclamarii(k)*semnulExclamarii(n-k))
    return int(result)

with open('comb_rezistoare.txt', 'r') as f:
    x = f.readline()

[n, M] = [int(readResult) for readResult in x.split()]

start = 0   
tmp = 0

while(tmp <= n):
    if(n < 0 or M < 0):
        start = 0
        break
    if(combinari(n, tmp) > M):
        start = tmp
        break
    else: # mai mic
        tmp = tmp + 1


print(start)
