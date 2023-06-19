arr = []
length = []
answer = ""
  
for _ in range(5):
  alpha = input()
  arr.append(alpha)
  length.append(len(alpha))
  
for i in range(max(length)):
  for j in range(5):
    if i < length[j]: # 만약 AABCDD, afzz가 있으면 패스해야하므로
      answer += arr[j][i]
      
print(answer)