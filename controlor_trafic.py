with open('controlor_trafic.txt', 'r') as f:
    max = int(f.readline())
    content = [int(x) for x in f.readline().split()]

# print(content)

sir = [x+1 for x in range(max)]
# print(sir)


result = []
for number in sir:
    if(number not in content):
        result.append(number)

# print(result)
final = 0
for nr in result:
    final = final + nr

print(final)