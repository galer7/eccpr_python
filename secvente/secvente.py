with open('secvente.txt', 'r') as f:
    intrari = f.readline()
    data = f.readlines()
    prag = float(data.pop().strip())
    numere = [float(item) for item in data]

# print(prag)
# print(numere)

binaryList = [1 if nr > prag else 0 for nr in numere]
# print(binaryList)

result = 0
sequenceCheck = False

for index, bit in enumerate(binaryList):
    if bit == 1 and sequenceCheck is False: # start sequence
        sequenceCheck = True
    if bit == 0 and sequenceCheck == True:
        result = result + 1
        sequenceCheck = False
    if bit == 1 and index == len(binaryList) - 1:
        result = result + 1

print(result)
        
