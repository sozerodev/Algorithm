class Solution:
    def hammingWeight(self, n: int) -> int:
        n_list = list(bin(n))
        
        cnt = 0
        for i in range(len(n_list)):
            if n_list[i] == "1":
                cnt += 1
            
        return cnt