with open('bingo.txt', 'r') as f:
    data = f.readlines()
    totalMatrice = int(data[0][0]) * int(data[0][0])
    [matrice, strigate] = [data[1].strip().split(), data[2].strip().split()]
    # print(type(matrice))
    # print(type(strigate))

counter = 0

for numar in matrice:
    if(numar in strigate):
        continue
    else:
        # print(numar)
        counter = counter + 1
    
if(counter == 0):
    print('BINGO!')
    
else:
    print(counter)