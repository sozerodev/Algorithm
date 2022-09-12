N = input()
S = input()


result = 0
default_point = 0

for num in range(len(S)):

    if S[num] == 'O':
        result += num+1+default_point

        default_point += 1

    else:
        default_point = 0


print(result)        

