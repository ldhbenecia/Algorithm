# n이 27일 때 27 -> 9 -> 3
# 3에서 return
# 그 다음 star(9) 실행
# 그 다음 star(27) 실행

def star(n):
  # 종료 조건
  if n == 3:
    return ["***", "* *", "***"]
  
  arr = star(n // 3)
  stars = []

  for i in arr:
    stars.append(i * 3)
  
  for i in arr:
    stars.append(i + " " * (n//3) + i)

  for i in arr:
    stars.append(i * 3)
    
  return stars

n = int(input())
print("\n".join(star(n)))