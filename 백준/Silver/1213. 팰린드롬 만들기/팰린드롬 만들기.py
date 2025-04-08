name = input()

dic = {}
for i in name:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

odd_cnt = 0
mid = ""

for i in sorted(dic.keys()):
    if dic[i] % 2 == 1:
        odd_cnt += 1
        mid = i  # 홀수 문자는 중앙 위치 지정

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
    exit()

half = ""
for i in sorted(dic.keys()):
    half += i * (dic[i] // 2)

print(half + mid + half[::-1])
