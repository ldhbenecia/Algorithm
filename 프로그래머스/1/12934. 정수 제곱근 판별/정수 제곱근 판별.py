def solution(n):
    if int(n ** (1/2)) == n ** (1/2):
        return ((n ** (1/2)) + 1) ** 2
    else:
        return -1    