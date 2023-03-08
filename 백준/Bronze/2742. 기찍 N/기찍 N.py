input = open(0).readline
def solution():
    print("\n".join(map(str, range(int(input()), 0, -1))))

if __name__ == '__main__': 
    solution()