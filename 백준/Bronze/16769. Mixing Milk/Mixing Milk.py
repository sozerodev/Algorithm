def solution():
    
    c_arr, m_arr = [0 for _ in range(3)], [0 for _ in range(3)]
    for i in range(3):
        c_arr[i], m_arr[i] = map(int, input().split())

    
    for i in range(100):
        idx, nxt = i % 3, (i+1)%3
        
        m_arr[idx], m_arr[nxt] = max(m_arr[idx] - (c_arr[nxt] - m_arr[nxt]), 0),min(c_arr[nxt], m_arr[idx]+m_arr[nxt])

    for i in m_arr:
        print(i)


if __name__ == '__main__': 
    solution()