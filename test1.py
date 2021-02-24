sample = []
output = []
for i in range(int(input())):
    sample.append([])
    len = int(input())

    sample[i].extend(input().split(" "))
    for cube in range(len):
        if sample[i][0] >= sample[i][-1]:
            sample[i].pop(cube)

print(sample)