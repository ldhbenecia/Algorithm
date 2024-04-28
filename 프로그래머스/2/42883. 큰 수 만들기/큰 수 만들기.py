def solution(number, k):
    stack = []
    
    for i in number:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    
    if k != 0:
        stack = stack[:-k]
        
    return ''.join(stack)

# 알고리즘
# number 값을 한 자리씩 순회
# stack에 값을 삽입
# 마지막 자리 값이 현재 값보다 작으면 비우고 대체
# k가 0이 될때까지