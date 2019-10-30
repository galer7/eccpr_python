with open('decodare_date.txt', 'r') as f:
    size = int(f.readline())
    content = []
    for line in f.readlines():
        content.append(line.strip())

# print(content)
new_content = [[] for i in range(size)]

for index, line in enumerate(content):
    current_line = line.split(',') # linia curenta cu split
    for ind2, elem in enumerate(current_line):
        if(elem.split('(')[0] == ''): # inseamna ca scriem elem[1:] si apoi (counter) de 0
            new_content[index].append(elem[1:])
            counter = int(current_line[ind2+1].split(')')[0]) # trebuie sa stim cat de mare e while-ul
            while(counter):
                new_content[index].append('0')
                counter = counter - 1
        elif(elem.split(')')[-1] == ''): # am trecut prin el pasul precedent
            continue
        else:
            new_content[index].append(elem) # daca nu are paranteza, scrie-l normal

# print(new_content)

for line in new_content:
    new_line = ','.join(line)
    print(f'{new_line}')