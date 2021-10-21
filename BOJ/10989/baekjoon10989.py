import sys

n = int(sys.stdin.readline())
lst = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    lst[num] += 1
# 예를 들어 1, 2, 2를 입력
# lst[1]은 2, lst[2]는 2가 된다.

for i in range(10001):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)
# 1부터 10001까지 반복문을 돌리는데
# 만약 lst[i]가 0이 아닐경우 -> 1, 2, 2를 입력했으므로 lst[1] = 1, lst[2] = 2이기 때문에 0이 아님
# 이럴 경우 그 다음 for문에서 range(lst[i])가 range(1), range(2)로 각각 됨
# 그래서 pirnt(i)에서 range(1)인 경우 i는 1이 한번, range(2)인 경우에는 i가 두번 반복하여 2가 두번 출력