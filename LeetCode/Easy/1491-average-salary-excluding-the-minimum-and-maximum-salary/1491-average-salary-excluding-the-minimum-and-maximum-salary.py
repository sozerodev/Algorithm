class Solution:
    def average(self, salary: List[int]) -> float:
        salary_sorted = sorted(salary)
        salary_lst = salary_sorted[1:-1]
        
        return sum(salary_lst)/len(salary_lst)

