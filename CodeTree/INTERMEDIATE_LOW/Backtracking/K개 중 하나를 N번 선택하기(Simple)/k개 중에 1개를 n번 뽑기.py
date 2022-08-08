k, n = tuple(map(int, input().split()))
answer = []

def print_answer():
    for i in answer:
        print(i, end = ' ')
    print()

def select(cnt):
    if cnt == n:
        print_answer()
        return

    for i in range(1, k+1):
        answer.append(i)
        select(cnt+1)
        answer.pop()

select(0)