n = int(input())
m = int(input())
num = sorted(list(map(int, input().split())))

# 입력 값이 굉장히 크기 때문에 최적화를 해야할 것으로 추정
# 이진 탐색으로 풀이하려고 했으나 2개씩 고정 -> 슬라이딩 윈도우 or 투포인터

left = 0
right = n - 1

result = 0
while left < right:
    temp = num[left] + num[right]

    if temp < m:
        left += 1
    elif temp > m:
        right -= 1
    else:
        result += 1
        left += 1
        right -= 1

print(result)
