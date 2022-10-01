N, M = map(int, input().split())

idol_info = {}
for team in range(N):
    team_name, member_len = input(), int(input())
    
    idol_info[team_name] = []
    for i in range(member_len):
        idol_info[team_name].append(input())

for q in range(M):
    q_answer, q_type = input(), int(input())
    for key, value in idol_info.items():
        if q_answer in value or q_answer == key:
            if q_type:
                print(key)
            else:
                for member in sorted(value):
                    print(member)
