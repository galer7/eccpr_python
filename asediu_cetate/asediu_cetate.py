with open('asediu_cetate.txt', 'r') as f:
    [nrWords, nrSoldati, start] = [int(x) for x in f.readline().split()]

# print(nrWords, nrSoldati, start)
soldati = []
for i in range(1, nrSoldati+1):
    soldati.append(i)

words = []
for i in range(1, nrWords+1):
    words.append(i)

# print(f'words: {words} and start from: {start}')


currentLocation = start - 1 # index of list
maxSoldati = nrSoldati
step = nrWords - 1

while(len(soldati) > 1):
    
    currentLocation = currentLocation + step # index

    if(currentLocation >= len(soldati)):
        currentLocation = currentLocation % len(soldati)

    soldati.remove(soldati[currentLocation])

print(soldati[0])