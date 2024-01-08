n = int(input())

def factorial(start):
  if start <= 0:
    return 1
  else:
    answer = start * factorial(start-1)
    return answer
  
print(factorial(n))