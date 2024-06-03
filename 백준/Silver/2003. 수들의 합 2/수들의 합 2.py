n, m = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 1

count = 0
while end <= n:
  total = sum(A[start:end])
  
  if total < m:
    end += 1
  elif total > m:
    start += 1
  else:
    count += 1
    end += 1
    
print(count)