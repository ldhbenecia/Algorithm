def jump(n): # n층에 도달하는 경우의 수를 return
  A = [0] * (n+1)
  answer = 0
  
  A[1] = 1
  A[2] = 2
  
  for i in range(3, n+1):
    A[i] = A[i-1] + A[i-2]
    
  answer = A[n]
  return answer

print(jump(7))