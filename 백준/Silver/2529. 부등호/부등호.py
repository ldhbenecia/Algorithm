def valid(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b

def dfs(depth, num):
    if depth == k + 1:
        lst.append(num)
        return
    
    for i in range(10):
        if not visited[i]:
            # 마지막 숫자와 0부터 9까지의 수를 비교해서 차근차근 쌓아감
            if depth == 0 or valid(num[-1], str(i), sign[depth - 1]):
                visited[i] = 1
                dfs(depth + 1, num + str(i))
                visited[i] = 0

k = int(input())
sign = list(input().split())
visited = [0] * 10

lst = []
dfs(0, '')

print(lst[-1])
print(lst[0])
