
def isPrime(x):
    inc = 0
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

with open('imagini_prime.txt', 'r') as f:
    lines = int(f.readline())
    cols = int(f.readline())
    content = [int(x) for x in f.read().split()]

result = [0 for chestie in content]
inc = 0
for index, elem in enumerate(content):
    # print(elem)
    if(not isPrime(elem)):
        inc = inc + 1

# print(content)
print(inc)