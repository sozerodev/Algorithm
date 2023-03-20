words = input().lower()
li = list(set(words))
cnt_li = []

for i in li:
    cnt = words.count(i)
    cnt_li.append(cnt)

if cnt_li.count(max(cnt_li)) >= 2:
    print("?")
else:
    print(li[cnt_li.index(max(cnt_li))].upper())