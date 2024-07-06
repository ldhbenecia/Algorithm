n = int(input())
nums = list(map(int, input().split()))

stack = []
turn = 1
for i in range(len(nums)):
    stack.append(nums[i])

    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

if not stack:
    print("Nice")
else:
    print("Sad")
