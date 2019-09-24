
with open('filtru_cuvinte.txt', 'r') as f:
    content = f.readline().strip('\n')
    x = f.readline().strip('\n')
    y = f.readline().strip('\n')

    cuvinte_cheie = y.split()

if(len(cuvinte_cheie) == int(x)):
    pass

firstContent = content
# print(content)
# print(x)
# print(cuvinte_cheie)

content = [elem for elem in content.split()]
# print(f'content: {content}')


for word in cuvinte_cheie:
    for i, word2 in enumerate(content):
        if word in word2:
            content[i] = word2.replace(str(word), ''.join(['*' for letters in word]))
            # print(word2)

# print(f'content after processing: {content}')


with open('filtru_cuvinte_result.txt', 'w') as f:
    f.write(' '.join(content))
    f.write('\n')