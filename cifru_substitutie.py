with open('cifru_substitutie.txt', 'r') as f:
    text = f.readline().strip()
    dict = f.readline().strip()

text = [x for x in text]
dict = [chestie for chestie in dict.split()]

dict = [[x.split(',')[0], x.split(',')[1]] for x in dict ]

print(text)
# print(dict)

for ind, litera in enumerate(text):
    for pair in dict:
        if(litera is pair[0]):
            text[ind] = pair[1]
            break

print(''.join(text))
