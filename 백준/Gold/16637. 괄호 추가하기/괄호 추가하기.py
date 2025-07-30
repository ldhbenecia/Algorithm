def calculator(op1, op2, operator):
    op1 = int(op1)
    op2 = int(op2)

    if operator == "+":
        return op1 + op2
    if operator == "-":
        return op1 - op2
    if operator == "*":
        return op1 * op2


def dfs(idx, current):
    global result

    # base
    if idx == n - 1:
        result = max(result, current)
        return

    # 괄호없이 계산: 현재 값과 다음 숫자 값 연산
    if idx + 2 < n:
        next = calculator(current, formula[idx + 2], formula[idx + 1])
        dfs(idx + 2, next)

    # 괄호를 먼저 계산: 다음 연산을 먼저 계산한 후 현재 값과 다시 계산
    if idx + 4 < n:
        next = calculator(
            current,
            calculator(formula[idx + 2], formula[idx + 4], formula[idx + 3]),
            formula[idx + 1],
        )
        dfs(idx + 4, next)


n = int(input())
formula = list(input())
result = float(-1e9)

dfs(0, int(formula[0]))
print(result)
