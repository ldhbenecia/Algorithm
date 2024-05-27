s = input()

count0 = 0
count1 = 0

# 첫 글자가 1이면 0으로 뒤집어야하므로 0 추가
if s[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(s) - 1):
  if s[i] != s[i + 1]:
    if s[i + 1] == '1':
      count0 += 1
    else:
      count1 += 1

print(min(count0, count1))

# 전부 0으로 바꾸는 횟수, 1로 바꾸는 횟수 중 적은 계산 구하기