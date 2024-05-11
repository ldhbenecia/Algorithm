def binary_search(array, target):
  array.sort()
  
  left = 0
  right = len(array)
  
  while left <= right:
    mid = (left + right) // 2
    
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      left += 1
    else:
      right -= 1
      
  return None

n = int(input())
array = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  result = binary_search(array, i)
  if result:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')


"""
5
8 3 7 9 2
3
5 7 9
"""
