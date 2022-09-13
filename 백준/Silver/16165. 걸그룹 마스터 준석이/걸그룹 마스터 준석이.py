N, M = map(int, input().split())

idol_info = {}
for team in range(N):
    team_name = input()

    member_len = int(input())
    idol_info[team_name] = []
    for i in range(member_len):
        idol_info[team_name].append(input())

    idol_info[team_name] = sorted(idol_info[team_name])

for q in range(M):
    q_answer = input()
    q_type = int(input())


    for key, value in idol_info.items():
        if q_answer in value or q_answer == key:
            if q_type == 0:
                for member in value:
                    print(member)
            else:
                print(key)

