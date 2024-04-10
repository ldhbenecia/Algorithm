cnt = 0

def dfs(numbers, target, current, idx):
    global cnt
    if len(numbers) == idx:
        if current == target:
            cnt += 1
        return cnt
    
    dfs(numbers, target, current + numbers[idx], idx + 1)
    dfs(numbers, target, current - numbers[idx], idx + 1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt