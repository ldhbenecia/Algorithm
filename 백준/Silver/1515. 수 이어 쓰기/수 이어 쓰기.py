import sys

nums = sys.stdin.readline().strip()

result = 0
idx = 0
flag = False
while not flag:
    result += 1
    for i in str(result):
        if nums[idx] == i:
            idx += 1
            if idx >= len(nums):  # 234092는 result가 20에 달했을 때 마침
                flag = True
                break

print(result)
