from collections import Counter
n = int(input())
nums = list(map(int, input().split()))
NGF = [-1] * n # -1로 초기화
cnt = Counter(nums)
stack = [0] # 0번 인덱스

for i in range(1, n):
    while stack and cnt[nums[stack[-1]]] < cnt[nums[i]]:
        NGF[stack.pop()] = nums[i]
    stack.append(i)

print(*NGF)

# count 메서드를 사용하였으나 시간초과가 나왔음
# count의 시간복잡도 = O(N)
# 이 문제에서 O(N)에다가 추가적인 연산이 들어가므로 입력 범위 값 1,000,000을 초과하게 됨
# 시간 초과를 해결하기 위해 nums의 카운트를 Counter로 처리 후 연산