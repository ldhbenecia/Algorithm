n = int(input())
nums = list(map(int, input().split()))
x = int(input())

# 값의 범위를 보니 이중 for문 시에 시간 초과
# 투 포인터로 처리
nums.sort()
start = 0
end = n - 1
result = 0

while start < end:
    s = nums[start] + nums[end]
    if s == x:
        result += 1
        start += 1
        end -= 1
    elif s < x:
        start += 1
    else:
        end -= 1

print(result)
