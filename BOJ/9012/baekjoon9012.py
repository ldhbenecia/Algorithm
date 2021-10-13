# 괄호 개수의 합으로 풀이
# 괄호 '('와 ')' 개수가 같으면 해결

n = int(input())

for _ in range(n):
    ps = list(input())
    sum = 0

    for i in ps:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0: # ')'이 먼저 나왔을 때 대비
            print("NO")
            break

    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
