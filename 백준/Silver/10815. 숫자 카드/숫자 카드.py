n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
validCard = list(map(int, input().split()))

def binary_search(array, target):
  start = 0
  end = len(array) - 1
  
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return "1"
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return "0"

result = []
for i in validCard:
  result.append(binary_search(card, i))

print(" ".join(result))