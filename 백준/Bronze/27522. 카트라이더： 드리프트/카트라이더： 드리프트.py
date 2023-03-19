input = open(0).readline
if __name__ == '__main__':
    result_lst = [[] for _ in range(8)]
    score = [10, 8, 6, 5, 4, 3, 2, 1]
    
    for i in range(8):
        time_str, team = input().split()
        min, sec, misec = map(int, time_str.split(":"))
        
        time = min*60 + sec + misec/1000
        result_lst[i] = (time, team)
    
    result_lst = sorted(result_lst)
    red_score, blue_score = 0, 0
    
    for i in enumerate(result_lst):
        if i[1][1] == "B":
            blue_score += score[i[0]]
        else:
            red_score += score[i[0]]
            
    if blue_score > red_score:
        print("Blue")
    else:
        print("Red")
        