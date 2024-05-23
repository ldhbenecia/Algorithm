import sys
input = sys.stdin.readline

p = int(input())

for _ in range(p):
  arr = list(map(int, input().split()))
  answer = 0
  for i in range(1, len(arr) - 1):
    for j in range(i + 1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        answer += 1

  print(arr[0], answer)