import sys
input = open(0).readline

sys.setrecursionlimit(10000)

def swap(arr, a, b):
    global change_cnt, K
    
    arr[a], arr[b] = arr[b], arr[a]
    
    change_cnt += 1
    if (change_cnt == K):
        print(f"{min([arr[a], arr[b]])} {max([arr[a], arr[b]])}")
        sys.exit(0)

def quickSort(arr, left, right):
    if left < right: # left가 더 크면 배열 범위가 정상적이지 않기 때문
        pivot = divide(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)

    
def divide(arr, left, right):
    """
    정렬된 피벗의 위치를 리턴함
    """
    
    x=arr[right];    # 기준원소
    i=left - 1;  
    for j in range(left, right): 
        if (arr[j] <= x):
            i += 1
            swap(arr, i, j)
    if (i + 1 != right):
        swap(arr, i + 1, right)
    return i + 1
    
if __name__ == '__main__':
    
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    change_cnt = 0
    
    a = quickSort(A, 0, N-1)
    print(-1)
        
        
        