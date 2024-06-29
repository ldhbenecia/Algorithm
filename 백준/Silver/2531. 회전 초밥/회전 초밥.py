import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

dic = defaultdict(int)
dic[c] = 1 # 쿠폰 사용해서 먹는 가짓 수 확정 포함
for i in range(k):
  dic[sushi[i]] += 1

start = 0
end = k - 1
answer = -1e9
while start < n:
  current_types = len(dic.keys()) # 현재 먹을 수 있는 초밥 가짓수
  answer = max(answer, current_types)
  
  # Move the window
  dic[sushi[start]] -= 1 # 윈도우의 왼쪽 끝 초밥을 제거
  if dic[sushi[start]] == 0:
      del dic[sushi[start]]
  start += 1
  end += 1
  dic[sushi[end % n]] += 1 # 윈도우의 오른쪽 끝 초밥 추가
  
print(answer)
