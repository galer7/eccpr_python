with open('campionat_fotbal.txt', 'r') as f:
    nrEchipe = int(f.readline())
    nrMeciuri = int(f.readline())
    meciuri = [x.strip() for x in f.readlines()]

scoruri = []

# init list:

for meci in meciuri:
    scoruri.append(meci.split()[0])
    scoruri.append(meci.split()[4])

scoruri = list(set(scoruri))
echipe = scoruri[:]

# print(meciuri)


for index, meci in enumerate(scoruri):
    scoruri[index] = [meci, 0, 0, 0]

# print(echipe)
# print(scoruri)

for meci in meciuri:
    for index, echipa in enumerate(echipe):
        # print(f'{meci.split()}')
        # index intre echipe si scoruri coincide pt fiecare tara
        if(echipa in meci.split()):
            index2 = meci.split().index(echipa) # gasim pe ce pozitie din titlul meciului se afla echipa
            # print(index2)
            if(index2 == 0):
                # echipa gazda
                scoruri[index][2] = scoruri[index][2] + int(meci.split()[1]) # goluri date
                scoruri[index][3] = scoruri[index][3] + int(meci.split()[3]) # goluri primite

                if(int(meci.split()[1]) > int(meci.split()[3])):
                    # win
                    scoruri[index][1] = scoruri[index][1] + 3
                elif(int(meci.split()[1]) == int(meci.split()[3])):
                    # draw
                    scoruri[index][1] = scoruri[index][1] + 1
                else:
                    continue

            if(index2 == 4):
                # echipa oaspete
                scoruri[index][3] = scoruri[index][3] + int(meci.split()[1]) # goluri primite
                scoruri[index][2] = scoruri[index][2] + int(meci.split()[3]) # goluri date

                if(meci.split()[1] < meci.split()[3]):
                    # win
                    scoruri[index][1] = scoruri[index][1] + 3
                elif(meci.split()[1] == meci.split()[3]):
                    # draw
                    scoruri[index][1] = scoruri[index][1] + 1
                else:
                    continue


scoruri.sort(key = lambda x: -x[1])

for scor in scoruri:
    print(f'{scor[0]} {scor[1]} {scor[2]} {scor[3]}')