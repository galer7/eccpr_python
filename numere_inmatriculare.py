nr_inmatriculare = ['AB', 'AR', 'AG', 'B', 'BC', 'BH', 'BN', 'BT', 'BV', 'BR', 'BZ', 'CS', 'CL', 'CJ', 'CT', 'CV', 'DB', 'DJ', 'GL', 'GR', 'GJ', 'HR', 'HD', 'IL', 'IS', 'IF', 'MM', 'MH', 'MS', 'NT', 'OT', 'PH', 'SM', 'SJ', 'SB', 'SV', 'TR', 'TM', 'TL', 'VS', 'VL', 'VN']

with open('numere_inmatriculare.txt', 'r') as f:
    data = f.readlines()
    # print(data)

for line in data:
    [oras, nr, litere] = [s.strip() for s in line.split()]
    
    if(oras == oras.upper() and oras in nr_inmatriculare):
        # oras e ok scris
        pass
    else:
        continue

    if(len(nr) >= 2 and len(nr) <= 3):
        try:
            if(type(int(nr)) == 'Integer'):
                pass
        except:
            continue
    else:
        continue
    

    leave = 0
    if(litere == litere.upper()):
        for litera in litere:
            if(not litera.isalpha()):
                leave = 1
        if(leave == 1):
            continue
        else:
            pass
    else:
        continue

    print(f'{oras} {nr} {litere}')
# print(int('a'))
