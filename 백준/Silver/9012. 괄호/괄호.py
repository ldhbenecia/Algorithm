# 시간 복잡도 신경 x
# 왼쪽 괄호와 오른쪽 괄호가 맞게 떨어져서 left = 0이 되면 VPS
# 그게 아닐 시 VPS가 아님
n = int(input())

for i in range(n):
  ps = list(input())
  left = 0
  
  for j in ps:
    if j == "(":
      left += 1
    elif j == ")":
      left -= 1
    
    # 이전에 (가 더 있었을 때, ())의 경우 left < 0, VPS 아님
    if left < 0:
      print("NO")
      break
  
  if left == 0:
    print("YES")
  elif left > 0:
    print("NO")
