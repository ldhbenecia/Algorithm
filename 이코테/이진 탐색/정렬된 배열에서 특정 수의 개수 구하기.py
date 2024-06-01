def first_position(start, end, target):
  while start <= end:
    mid = (start + end) // 2
    
    # target을 찾았을 때 (이제 제일 왼쪽 값인지 비교해야 함)
    if lst[mid] == target:
      # mid == 0에 대한 처리와 mid - 1이 target이 다르면 제일 왼쪽값이라는 뜻
      if mid == 0 or target != lst[mid - 1]:
        print("시작하는 위치", mid)
        return mid
      # 제일 왼쪽 값이 아닌 경우 end를 줄임
      else:
        end = mid - 1
    # target보다 뒤에 있는 경우
    elif lst[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1
      
  return -1

def last_position(start, end, target):
  while start <= end:
    mid = (start + end) // 2
    # target을 찾았을 때 (이제 제일 오른쪽 값인지 비교해야 함)
    if lst[mid] == target:
      # mid에 대한 처리와 mid + 1이 target이 다르면 제일 오른쪽값이라는 뜻
      if mid == len(lst) -1 or target != lst[mid + 1]:
        print("마지막 위치", mid)
        return mid
      else:
        start = mid + 1
    elif lst[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1
      
  return -1

n, x = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = len(lst) - 1

if x not in lst:
  print(-1)
else:
  print(last_position(start, end, x) - first_position(start, end, x) + 1)


# lst는 처음부터 오름차순으로 주어진다.
# 고로 x값이 발견되었을 때 x값이 1개 이상일 경우 그 뒤의 값도 x일 것이다.
# x값이 나오는 첫 위치와 마지막 위치를 구해서
# 마지막 위치 값 - 첫 위치 값
# 시간 복잡도 O(logN)으로 설계하지 않을 경우 '시간 초과' 판정

"""
7 2
1 1 2 2 2 2 3

4
-------------
7 4
1 1 2 2 2 2 3

-1
"""
