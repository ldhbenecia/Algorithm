N = int(input())
top = list(map(int, input().split()))

# 이중 for문 불가능 (시간복잡도)
result = [0] * N
stack = []  # idx, height
for i in range(len(top)):
    while stack and stack[-1][1] <= top[i]:
        stack.pop()

    # 스택 top이 가장 가까운 "왼쪽이 더 큰 탑"
    if stack:
        result[i] = stack[-1][0]

    stack.append((i + 1, top[i]))

print(*result)
