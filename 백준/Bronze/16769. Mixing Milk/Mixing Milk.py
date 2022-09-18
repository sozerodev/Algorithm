def solution():
    
    c_arr, m_arr = [], []
    for _ in range(3):
        c, m = map(int, input().split())

        c_arr.append(c)
        m_arr.append(m)

    
    for i in range(100):
        idx = i % 3
        nxt = (i+1)%3
        
        m_arr[idx], m_arr[nxt] = max(m_arr[idx] - (c_arr[nxt] - m_arr[nxt]), 0), min(c_arr[nxt], m_arr[idx]+m_arr[nxt])

    for i in m_arr:
        print(i)

if __name__ == '__main__':
    solution()