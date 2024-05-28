n, m = map(int, input().split())
weight = list(map(int, input().split()))

# 1 <= M <= 10
arr = [0] * 11

# 각 무게에 해당하는 볼링공 개수 카운트
for i in weight:
  arr[i] += 1
  
count = 0
for i in range(1, m + 1):
  n -= arr[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  count += arr[i] * n # B가 선택하는 경우의 수와 곱하기
  
print(count)


# 완전 탐색 풀이 (직접 풀이)
'''
n, m = map(int, input().split())
weight = list(map(int, input().split()))

count = 0
for i in range(len(weight)):
  for j in range(i + 1, len(weight)):
    if weight[i] != weight[j]:
      count += 1
    
print(count)
'''

'''
5 3
1 3 2 3 2

8
----------
8 5
1 5 4 3 2 4 5 2

25
'''
