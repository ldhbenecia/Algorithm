n = int(input())
nums = sorted(list(map(int, input().split())))

answer = 0

for i in range(n):
  tmp = nums[:i] + nums[i + 1:] # 좋은 수 인지 확인할 값 제외한 리스트
  start = 0
  end = len(tmp) - 1
  
  while start < end:
    temp = tmp[start] + tmp[end] # 투 포인터로 합산
    
    if temp == nums[i]: # 만약 다른 두 수로 나타낼 수 있는 값이라면 좋은 수
      answer += 1
      break
    
    if temp < nums[i]:
      start += 1
    else:
      end -= 1

print(answer)