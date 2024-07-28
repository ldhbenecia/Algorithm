n = int(input())
nums = list(map(int, input().split()))

left = 0
right = 0
result = 0
dic = {}
while right < n:
    if nums[right] in dic:
        dic[nums[right]] += 1
    else:
        dic[nums[right]] = 1

    while len(dic) > 2:
        dic[nums[left]] -= 1
        if dic[nums[left]] == 0:
            del dic[nums[left]]
        left += 1

    result = max(result, right - left + 1)
    right += 1

print(result)
