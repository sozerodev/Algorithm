N = int(input())

for i in range(1, N + 1):
    print(f"{'*'*i}{' '*(N-i)}", end="")
    print(f"{' '*(N-i)}{'*'*i}")
    
    
for i in range(N-1, 0, -1):
    print(f"{'*'*i}{' '*(N-i)}", end="")
    print(f"{' '*(N-i)}{'*'*i}")
