input = open(0).readline
def solution():

    X, Y = map(int, input().split())
    
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    type1 = [1, 3, 5, 7, 8, 10]
    type2 = [4, 6, 9, 11]
    
    sum = 0
    for i in range(1, X):
        if i in type1:
            sum += 31
        elif i in type2:
            sum += 30
        else:
            sum += 28
    sum += Y
    print(week[sum%7])
    
if __name__ == '__main__': 
    solution()

