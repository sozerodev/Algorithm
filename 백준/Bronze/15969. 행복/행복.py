student_num = input()
point_list = list(map(int, input().split()))
print(max(point_list) - min(point_list))
