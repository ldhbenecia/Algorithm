def is_valid(prev, curr, sign):
    if sign == "<":
        return prev < curr
    else:
        return prev > curr


def backtracking(depth, num):
    # base
    if depth == k + 1:
        result.append("".join(map(str, num)))
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or is_valid(num[depth - 1], i, signs[depth - 1]):
                visited[i] = True
                num.append(i)
                backtracking(depth + 1, num)
                num.pop()
                visited[i] = False


k = int(input())
signs = input().split()

result = []
visited = [False] * 10
backtracking(0, [])

print(result[-1])
print(result[0])
