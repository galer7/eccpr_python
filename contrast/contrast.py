import math

contentCopy = []

def average(x):
    sum = 0
    for item in x:
        sum = sum + item
    result = sum/len(x)
    return result

with open('contrast.txt', 'r') as f:
    lines = int(f.readline())
    cols = int(f.readline())
    content = [int(x) for x in f.read().split()]
    contentCopy = content

matrix = [[0 for i in range(lines)] for j in range(cols)]
index = 0
# print(content)

for line in range(lines):
    for col in range(cols):
        matrix[line][col] = math.floor(content[index]*0.9 + 2)
        index = index + 1

results = [0 for x in contentCopy]
index = 0


for line in range(lines):
    for col in range(cols):
        results[index] = matrix[line][col] - contentCopy[index]
        index = index + 1

print(f'{average(results):.2f}')