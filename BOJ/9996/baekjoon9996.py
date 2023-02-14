n = int(input())
pattern = list(map(str, input().split("*"))) # 패턴

length = len(pattern[0]) + len(pattern[1])
left = pattern[0]
right = pattern[1]

for i in range(n):
  name = input() # 퍄일 이름
  
  if length > len(name): print("NE")
  
  else:
    if left == name[:len(left)] and right == name[-len(right):]: # 패턴의 * 앞 부분과 일치하고 * 뒷 부분과 일치하면
      print("DA")
    else:
      print("NE")
    
    
# 첫 값과 끝 값만이 아니라 ab*cd 이런 패턴이 오는 경우도 생각을 해야 함
# *을 기준으로 왼쪽과 오른쪽 값을 갈라야 함
# 만약 a*a가 패턴이고 a가 주어지면 a가 하나밖에 없기 때문에 중복이 될 수 없으므로 NE가 떠야 함
# 따라서 패턴의 총 길이가 파일 이름보다 클 경우 패턴이 일치할 수 없음