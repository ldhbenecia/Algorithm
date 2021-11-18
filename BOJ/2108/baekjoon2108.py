import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = list()

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))
    
num_list.sort()

# 산술 평균
avg = round(sum(num_list) / len(num_list))
print(avg)

# 중앙 값
print(num_list[n//2])

# 최빈 값
many_num = Counter(num_list).most_common(2)

if len(num_list) > 1:
    if many_num [0][1] == many_num[1][1]: #최빈 값이 여러개면
        print(many_num[1][0]) # 두번 째로 작은 값 출력
    else: # 최빈 값이 하나라면
        print(many_num[0][0]) # 첫번 째 값 출력(최빈 값)
else: # 같은 숫자가 한개만 여러번 주어졌을 경우
    print(num_list[0])   

# 범위
print(max(num_list) - min(num_list))