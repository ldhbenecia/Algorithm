n = int(input())
score_list = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n - 1, 0, -1):
  if score_list[i] <= score_list[i - 1]:
    minus_value = score_list[i - 1] - score_list[i] + 1 # 이전 값이랑 비교해서 1 큰거
    cnt += minus_value
    score_list[i - 1] = score_list[i] - 1 # 이전 값 변경
    
print(cnt)
