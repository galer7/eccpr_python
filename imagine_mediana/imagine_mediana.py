with open('imagine_mediana.txt', 'r') as f:
    n = int(f.readline())
    m = int(f.readline())

    matrice = [[0 for x in range(m)] for x in range(n)]
    for i in range(n):
        for j in range(m):
            matrice[i][j] = int(f.readline())
    

for row in matrice:
    row.insert(0, 0)
    row.append(0)

padding = [0 for x in range(m+2)]

matrice.insert(0, padding)
matrice.append(padding)

tmp = []
result = []

for i, row in enumerate(matrice):
    for j, col in enumerate(row):
        if i == 0 or j == 0 or i == n+1 or j == m+1:
            continue
        else:
            tmp.append(matrice[i][j])
            tmp.append(matrice[i][j+1])
            tmp.append(matrice[i+1][j])
            tmp.append(matrice[i-1][j])
            tmp.append(matrice[i][j-1])

            tmp.sort()
            result.append(tmp[2])
        tmp = []

for x in result:
    print(x)