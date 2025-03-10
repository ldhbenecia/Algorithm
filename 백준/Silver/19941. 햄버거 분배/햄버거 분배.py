n, k = map(int, input().split())
position = list(input())

result = 0
visited = [False] * n

for i in range(len(position)):
    if position[i] == "P":
        # 사람이 나왔을 때 그 사람으로부터 k만큼 좌우로 햄버거가 있느냐 없느냐, 있으면 result += 1
        # index 범위 오류가 일어날 수 있으니 앞에 값은 0이상, 끝에 값은 n 이하
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if position[j] == "H" and not visited[j]:
                visited[j] = True
                result += 1
                break

print(result)
