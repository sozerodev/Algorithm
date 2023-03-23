def solution(nums):
    choose_num = len(nums)//2
    
    monsters = list(set(nums))
    
    if len(monsters)<choose_num:
        return len(monsters)
    else:
        return choose_num
    