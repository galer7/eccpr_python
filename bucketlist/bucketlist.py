with open('bucketlist.txt', 'r') as f:
    f.readline()
    content = f.readline()

content = [int(x) for x in content.split()]
# print(content)

buckets = [[1+x, []] for x in range(19)]
# print(buckets)

for number in content:
    for bucket in buckets:
        # print(pow(10,bucket[0]-1), pow(10,bucket[0])-1)
        if(number >= pow(10, bucket[0]-1) and number < pow(10, bucket[0])-1):
            bucket[1].append(number)

# print(buckets)

for bucket in buckets:
    if(len(bucket[1]) is not 0):
        print(f'{bucket[0]} {len(bucket[1])}')
