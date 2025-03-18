n = int(input())
larger = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    cnt = 0 # 왼쪽 키 큰 사람 수
    for j in range(n):
        if cnt == larger[i] and result[j] == 0: # 키 큰 사람 수 맞고 자리가 비어있다면
            result[j] = i + 1 # 삽입
            break
        elif result[j] == 0: # 키 큰 사람 수 다르고 자리 비었으면 카운트
            cnt += 1

print(*result)
