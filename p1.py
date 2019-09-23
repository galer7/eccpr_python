
i=0
with open('p1input.txt', 'r') as f:
    line1 = f.readline()
    # print(line1)
    [firstLetter, lastLetter, minLength, maxLength] = line1.split()
    
    line2 = f.readline().split()
    counter = [0, 0, 0]
    for word in line2:
        if(word[0].lower() == firstLetter.lower() and word[-1].lower() == lastLetter.lower()):
            if(len(word) < int(minLength)):
                counter[0] = counter[0] + 1
            elif(len(word) >= int(minLength) and len(word) < int(maxLength)):
                counter[1] = counter[1] + 1
            elif(len(word) >= int(maxLength)):
                counter[2] = counter[2] + 1

print(f'{counter[0]} {counter[1]} {counter[2]}')