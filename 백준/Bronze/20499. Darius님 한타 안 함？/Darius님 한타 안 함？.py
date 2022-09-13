K, D, A = map(int, input().split("/"))

# if K + A < D or D == 0:
#     print("hasu")
# else:
#     print("gosu")

# 위를 이렇게 한줄로 줄일 수 있다. 
print("hasu") if K + A < D or D == 0 else print("gosu")
