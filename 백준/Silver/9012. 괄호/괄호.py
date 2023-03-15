input = open(0).readline

if __name__ == '__main__':
    
    # 풀이1
    # open된 괄호의 수와 close 괄호의 수를 더하고 빼면 될거라 생각했는데
    # 좀 복잡한거같다 괜히
    for i in range(int(input())):
        input_vps = input().strip()
        
        open_vps = 0
        for string in input_vps:
            if string == "(":
                open_vps += 1
            else:
                open_vps -= 1
        
            if open_vps < 0:
                break
                
        if open_vps != 0:
            print("NO")
        else:
            print("YES")      
        
        
    # 풀이 2
    # () 괄호를 그냥 없애기
    # for _ in range(int(input())):
    #     s = input().strip()
    #     while '()' in s:
    #         s = s.replace('()','')
        
    #     print('NO') if s else print('YES')