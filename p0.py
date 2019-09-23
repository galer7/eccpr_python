with open('p0input.txt', 'r') as f:
    x = f.readline()
# x = input()

words = x.split()
# print(words)

for word in words[:]:
    if(word != word.lower()):
        word = word.lower()
        # print(f'{word} removed!')

result = []

words2 = words
while(len(words) > 0):
    for word in words[:]:
        counter = 0
        for word2 in words2[:]:
            if(word.lower() == word2.lower()):
                words2.remove(word2)
                counter = counter + 1
        if(counter != 0):
            result.append([word.lower(), counter])

result.sort(key = lambda x: (-x[1], x[0]))
# result.sort()
# print(result)

for pair in result:
    [word, nr] = pair
    print(f'{word} {nr}')