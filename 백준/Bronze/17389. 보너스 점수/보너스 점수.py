N, S = input(), input()

# 풀이 1
# result = 0
# default_point = 0

# for num in range(len(S)):
#     if S[num] == 'O':
#         result += num+1+default_point
#         default_point += 1

#     else:
#         default_point = 0

# print(result)        


# 풀이 2
score, bonus = 0, 0

for idx, OX in enumerate(S):
    # enumerate를 쓰면 idx와 value를 함께 얻을 수 있다. 
    if OX == "O":
        # score += idx + 1 + bonus
        # bonus += 1
        score, bonus = score + idx + 1 + bonus, bonus + 1
    
    else:
        bonus = 0  

print(score)


