input = open(0).readline

if __name__ == '__main__':
    
    for i in range(int(input())):
        input_vps = input().strip()
        
        open_vps = 0
        for string in input_vps:
            if string == "(":
                open_vps += 1
            else:
                open_vps -= 1
        
            if open_vps < 0:
                print("NO")
                break
                
        if open_vps < 0:
            continue
        if open_vps != 0:
            print("NO")
        else:
            print("YES")      
        