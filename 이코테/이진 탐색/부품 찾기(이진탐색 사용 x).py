#def binary_search(array, left, right, target):
  
# 이진 탐색 안 쓴 풀이
n = int(input())
array = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

lst = []

for i in x:
  if i in array:
    lst.append('yes')
  else:
    lst.append('no')
    
print(*lst)