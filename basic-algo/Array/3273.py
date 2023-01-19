n = int(input())
num_list = sorted(list(map(int, input().split())))
x = int(input())

ans = 0
left, right = 0, n - 1

while left < right:
  result = num_list[left] + num_list[right]
  
  if result == x:
    ans += 1
    left += 1
  elif result < x:
    left += 1
  else: 
    right -= 1
print(ans)

# 투 포인터를 사용하여 풀이
# 이중 for문을 사용하지 않는다.

# 1. 리스트를 오름차순으로 정렬
# 2. 리스트의 시작, 끝 지점부터 합산하여 비교
# 3. left, right를 더하였는데 찾고자하는 값보다 값이 작다면 작은 쪽인 left를 +=1 해서 크기를 늘림
# 4. 그 반대로 x 보다 result가 큰 경우에는 값이 크기 때문에 마지막 right를 한칸 앞으로 -= 1 당겨주어 값을 줄임
# 5. left와 right가 교차하는 순간이 오면 모든 비교, 탐색은 끝