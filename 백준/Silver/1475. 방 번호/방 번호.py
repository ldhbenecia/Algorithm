n = int(input())
nums = [0] * 10

for i in str(n):
    num = int(i)
    if num == 6 or num == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[int(i)] += 1

print(max(nums))
