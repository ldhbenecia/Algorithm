n = int(input())
nums = list(map(int, input().split()))
NGE = [-1] * n # -1로 초기화
stack = [0] # 0번 인덱스

# 1번 인덱스부터 비교
for i in range(1, len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        NGE[stack.pop()] = nums[i]
    stack.append(i)
    
print(*NGE)
# nums의 원소가 1,000,000까지 주어질 수 있으므로 N^2 불가능

# 3 5 2 7
# stack[0] 상태
# stack이 있고 nums[stack[-1]] = nums[0] < nums[i] = 3 < 5(i는 1부터 시작)
# NGE[stack.pop()] = stack.pop()을 하면 인덱스 0이 나오고 NGE의 인덱스 0에 5로 변경
# stack에 1을 삽입하면서 stack[1] 상태
# 위와 같이 반복