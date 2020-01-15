class Farfurie:
    def __init__(self, denumire, order, tip):
        self.denumire = denumire
        self.order = order
        self.tip = tip

def orderFarfurie(x):
    if x == 'A':
        return 1
    if x == 'C':
        return 2
    if x == 'P':
        return 3
    if x == 'D':
        return 4

nrMeniuriComplete = 0
nrMeniuriUnknown = 0
nrFarfuriiRamase = 0

x = input()
farfuriiOld = x.split()
farfurii = [0 for x in farfuriiOld]

for ind, farfurie in enumerate(farfuriiOld):
    farfurii[ind] = Farfurie(farfurie[0], orderFarfurie(farfurie[0]), farfurie[1])
    
meniuCurent = []
for ind, farfurie in enumerate(farfurii):
    if ind == 0:
        meniuCurent.append([farfurie.order, farfurie.tip])
        continue
    
    # print(meniuCurent)

    if meniuCurent: # daca nu e gol meniul curent
        if farfurie.order > meniuCurent[-1][0]: # daca avem un fel principal care respecta ordinea de servire, adaugam in meniul curent
            meniuCurent.append([farfurie.order, farfurie.tip])
            continue    # iesim, din moment ce respecta regula. ATENTIE: trebuie testat in afara for-ului, si vazut daca mai ramane ceva in meniu dupa for.
        
        else: # daca meniul nu e gol si avem o farfurie care nu respecta regula. farfuria curenta o vom adauga in noul meniuCurent
            if len(meniuCurent) >= 2: # este un meniu valid
                if '0' in [x[1] for x in meniuCurent]: # daca avem vreo farfurie identificata
                    nrMeniuriUnknown += 1
                    nrMeniuriComplete += 1 
                else:
                    nrMeniuriComplete += 1 
                
            else: # nu este un meniu valid!
                nrFarfuriiRamase += len(meniuCurent)
                
            meniuCurent = [] # golim meniul,
            meniuCurent.append([farfurie.order, farfurie.tip]) # si adaugam farfuria care nu se potrivea inainte
            
    else: # daca meniul este gol
        meniuCurent.append([farfurie.order, farfurie.tip]) # adaugam farfuria
        continue # redundant
    
# print('dupa for:', meniuCurent)
if meniuCurent: # aici avem doar cazuri ok, insa trebuie sa verificam lungimea
    if len(meniuCurent) >= 2:
        if 0 in [x[1] for x in meniuCurent]: # daca avem vreo farfurie identificata
            nrMeniuriUnknown += 1
            nrMeniuriComplete += 1 
        else:
            nrMeniuriComplete += 1 
    else:
        nrFarfuriiRamase += len(meniuCurent)
    
    
print(nrMeniuriComplete)
print(nrMeniuriUnknown)
print(nrFarfuriiRamase)