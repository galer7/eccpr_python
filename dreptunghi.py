with open('dreptunghi.txt', 'r') as f:
    f.readline()
    content = [line.split() for line in f.readlines()]

def aria(arg):
    [x1, y1, x2, y2] = arg
    return abs(y2-y1)*(x2-x1)

max = 0
ind_max = 0
for index, copil in enumerate(content):
    curr_dreptunghi = [int(x) for x in copil[1:]]
    curr_aria = aria(curr_dreptunghi)
    if(curr_aria > max):
        max = curr_aria
        ind_max = index
    # print(curr_dreptunghi)


result = ' '.join(content[ind_max])
print(f'{result} {max}')