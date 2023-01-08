class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        

        product_digits = 1
        n_list = list(map(int, list(str(n))))
        
        for i in n_list:
            product_digits *= i



        sum_digits = sum(n_list)
        return product_digits - sum_digits

    