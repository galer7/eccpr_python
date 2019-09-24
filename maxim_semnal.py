with open('maxim_semnal.txt', 'r') as f:
    numarNumere = f.readline()
    valori = [float(x) for x in f.readlines()]

if(numarNumere == len(valori)):
    pass

# print(valori)
valori.append(0.0)

maxime = []

for index in range(len(valori)-1):
    # print(index)
    if(valori[index] > valori[index - 1] and valori[index] > valori[index + 1]):
        maxime.append(valori[index])

average = 0
for nr in maxime:
    # print(nr)
    average = average + nr

average = average / len(maxime)

counterFinal = 0

# print(average)
for valoare in valori:
    if(valoare > average):
        counterFinal = counterFinal + 1

print(f'{counterFinal}')