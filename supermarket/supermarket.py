with open('supermarket.txt', 'r') as f:
    content_size = f.readline()
    data = f.readlines()
    [db, scanned] = [[x.strip() for x in data[:-1]], data[-1]]

# print(db)
# print(scanned)

total = 0.00
reducere_curenta = 0

for item in scanned.split():
    for entry in db:
        [cod, tip_functie, content] = entry.split()
        print(cod, type(cod))
        print(item, type(item))
        if(item == cod):
            print('im in')
            if(tip_functie == 'p'):
                content = float(content)
                total = total + ((100-reducere_curenta)/100)*content
                reducere_curenta = 0
                break
            if(tip_functie == 'c'):
                content = int(content)
                print(reducere_curenta)
                reducere_curenta = reducere_curenta + content
                break

print(f'{total:.2f}')
