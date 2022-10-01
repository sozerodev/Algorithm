from sys import stdin
input = stdin.readline
def solution():
    user_dice = list(map(int, input().split()))
    
    # 중복 제거 된 list
    dice_num = list(set(user_dice))

    
    if (len(dice_num)==3):
        # 확률적으로 모두 다를 경우가 가장 클 것 같으니 여길 첫번째 if문으로 받는다
        return max(user_dice)*100
        
    elif (len(dice_num) == 2):
        for dice in dice_num:
            if (user_dice.count(dice) > 1):
                return 1000 + dice*100
    else:
        return 10000 + dice_num[0]*1000


if __name__ == '__main__': 
    print(solution())