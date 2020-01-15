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

<<<<<<< HEAD
while len(soldati) > 1:
    # print(f'{soldati} cu lungime {len(soldati)}')
=======
while(len(soldati) > 1):
    
>>>>>>> 9cc6f3bf52afb7c795379eba24fa8a4eba997b1d
    currentLocation = currentLocation + step # index

    if(currentLocation >= len(soldati)):
        currentLocation = currentLocation % len(soldati)

    soldati.remove(soldati[currentLocation])

print(soldati[0])