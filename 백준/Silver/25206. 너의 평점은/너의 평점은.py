score_table = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0
}

class_sum = 0.0
grade_sum = 0.0
for i in range(20):
    class_name, class_point, grade = input().split()
    
    if grade != 'P':
        class_sum += float(class_point)
        grade_sum += score_table[grade]*float(class_point)
    

# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
print(grade_sum/class_sum)


