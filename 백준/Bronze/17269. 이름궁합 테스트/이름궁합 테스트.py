# 지문에 주어진 변수가 있으면 똑같이 따라서 주는 편이 좋다.
N, M = map(int, input().split())
A, B = input().split()


# 코테는 의외로 이렇게 하나하나 적어줘야 하는 경우가 있다고 함
alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]


# 1. 문자열을 처리한다. 
AB = ''
min_len = min(N, M)

for i in range(min_len):
    AB += A[i] + B[i]

# 리스트[N:] 을 하면 N이 리스트의 길이보다 길어도
# index out of range에러가 뜨지 않고 빈 문자열을 반환한다.
AB += A[min_len:] + B[min_len:]

# 문자열을 하나씩 반복하면서..
# ord() : ASKII값 반환 
# alp에 해당하는 알파벳의 인덱스 값을 반환하게 될 것
lst = [alp[ord(i)- ord('A')] for i in AB]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]
        

print("{}%".format(lst[0]%10*10 + lst[1] % 10))

