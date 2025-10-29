import sys

input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

# 시간 제한 1초, N과 M의 범위는 100,000이므로 이중 for문 불가능
# 이진 탐색 사용

for t in targets:
    left = 0
    right = n - 1
    isFound = False

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == t:
            isFound = True
            break
        elif a[mid] < t:
            left = mid + 1
        else:
            right = mid - 1

    if isFound:
        print(1)
    else:
        print(0)
