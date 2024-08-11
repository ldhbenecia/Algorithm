from collections import Counter

n, c = map(int, input().split())
nums = list(map(int, input().split()))

cnt = Counter(nums).most_common()

result = []
for key, n in cnt:
    for i in nums:
        if i == key:
           result.append(i) 
           
print(*result)