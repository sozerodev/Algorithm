input_num, lst = int(input()), list(map(int, input().split()))


x_lst = [lst[0]]

for i in range(1, input_num):
    x = lst[i]*(i+1) - sum(x_lst)
    x_lst.append(x)


for j in x_lst:
    print(j, end=" ")
    