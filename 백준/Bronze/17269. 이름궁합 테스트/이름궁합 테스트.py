import copy

name_cnt = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1
}



name_len1, name_len2 = map(int, input().split())

name = list(map(str, input().split()))
name_sort = []

for i in range(min(name_len1, name_len2)):
    name_sort.append(name[0][i])
    name_sort.append(name[1][i])



if name_len1 > name_len2:
    longer_name = name[0]
else:
    longer_name = name[1]

for i in range(min(name_len1, name_len2), max(name_len1, name_len2)):
    name_sort.append(longer_name[i])


name_num = []
for i in name_sort:
    name_num.append(name_cnt[i])


name_temp = copy.deepcopy(name_num)

while (len(name_temp) >2):
    temp = []
    for i in range(len(name_temp) - 1):
        name_sum = name_temp[i] + name_temp[i+1]
        if name_sum > 9:
            temp.append(int(str(name_sum)[-1]))
            
        else:
            temp.append(name_sum)
            
    name_temp = temp


if (name_temp[0] == 0):
    print(f"{name_temp[1]}%")
else:
    print(f"{name_temp[0]}{name_temp[1]}%")