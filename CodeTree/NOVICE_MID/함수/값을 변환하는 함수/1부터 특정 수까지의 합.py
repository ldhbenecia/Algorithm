n = int(input())

def print_answer(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    result = sum // 10

    print(result)

print_answer(n)