def binary_search(left, right, target):
  while left <= right:
    total = 0
    mid = (left + right) // 2
    
    for i in nums:
      if i > mid:
        total += mid
      else:
        total += i
    
    if total > target:
      right = mid - 1
    else:
      left = mid + 1
      
  return right

n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())

left = 0
right = nums[-1]

print(binary_search(left, right, m))

# 시작점 0부터 끝점 nums[-1]을 초기값으로 잡는다.
# nums를 가지고 순회를 돌면서 중간 값보다 크다면 total에 특수 상한액(mid)를 더한다.
# nums 순회를 끝낸 후 m(target)과 비교하여 더 크면 상한액을 낮추고 작으면 높인다.