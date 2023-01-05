class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # odd_num = 0
        # for i in range(low, high + 1):
        #     if i % 2 != 0:
        #         odd_num += 1 
        # return odd_num
        if low % 2 == 1 or high % 2 == 1:
            return (high-low)//2 + 1
        else:
            return (high-low)//2