s = list(input())
s.sort()

answer = ''
num = 0
for i in s:
  if i.isnumeric():
    num += int(i)
  else:
    answer += i
    
answer += str(num)
print(answer)

'''
입력 예시
A1KA5CB7
AJKDLSI412K4JSJ9D

출력 예시
ABCKK13
ADDIJJJKKLSS20
'''