pi = 3.1415
mp = 1.67e-27
me = 9.11e-31

mp_min = mp*0.9
mp_max = mp*1.1

me_min = me*0.9
me_max = me*1.1

particule = []
with open('cern.txt', 'r') as f:

    [R, a, N] = [x for x in f.readline().split()]
    [R, a] = [float(R), float(a)]
    N = int(N)

    for line in f.readlines():
        particule.append(float(line))

mase = []
cunoscute = []
for particula in particule:
    tmp = (2/3000)*(particula/(a*pi*R))
    mase.append(tmp)
    
    if (tmp > mp_min and tmp < mp_max) or (tmp > me_min and tmp < me_max):
        cunoscute.append(particula)
    
for masa in mase:
    print(f'{masa:.6e}')

fractie = (N-len(cunoscute))/N
print(f'{fractie:.4f}')