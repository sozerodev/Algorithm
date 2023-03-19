input = open(0).readline

def fibonacci_one(n):
    global table
    if n < 2: 
        return n
    
    for i in range(2, n + 1):
        table[i] = table[i-2] + table[i-1]
        
    return table[n]

def fibonacci_zero(n):
    global table_zero
    if n == 0: 
        return 1
    elif n == 1:
        return 0
    
    for i in range(2, n + 1):
        table_zero[i] = table_zero[i-2] + table_zero[i-1]
        
    return table_zero[n]

if __name__ == '__main__':
    table = [0 for _ in range(41)]
    table[0], table[1] = 0, 1
    
    table_zero = [0 for _ in range(41)]
    table_zero[0], table_zero[1] = 1, 0
    
    for i in range(int(input())):
        N = int(input())
        print(fibonacci_zero(N), end= " ")
        print(fibonacci_one(N))