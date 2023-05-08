n = int(input())
num_list = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

num_list.sort()

def binary_search(target):
  start = 0
  end = len(num_list) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if num_list[mid] == target:
      return True
    
    if target < num_list[mid]:
      end = mid - 1
    elif target > num_list[mid]:
      start = mid + 1  
  
for i in range(m):
  if binary_search(check_list[i]):
    print(1)
  else:
    print(0)