input = open(0).readline

def solution():
    
    input_string = input()
    for i in range (len(input_string)//10 + 1):
        try:
            print(input_string[i*10: i*10 + 10])
        except:
            print(input_string[i*10: len(input_string)])
        
if __name__ == '__main__': 
    solution()

