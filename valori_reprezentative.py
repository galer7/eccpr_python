with open('valori_reprezentative.txt', 'r') as f:
    sir1 = []
    sir2 = []

    length1 = int(f.readline())
    for i in range(length1):
        sir1.append(int(f.readline()))
    
    length2 = int(f.readline())
    for i in range(length2):
        sir2.append(int(f.readline()))

# print(sir1)
# print(sir2)

sirFinal = sir1 + sir2
# print(sirFinal)

index = 5 - len(sirFinal)
sirAvg = []
sirFinal.sort()
print(sirFinal)

while(index < 0):
    sirAvg.append(sirFinal[index])
    index = index + 1

print(sirAvg)

answer = 0
for nr in sirAvg:
    answer = answer + nr

answer = answer/len(sirAvg)
print(f'{answer:.2f}')