n = int(input())

def print_answer(n):
    count = 1
    for _ in range(n):
        for _ in range(n):
            print(count, end = " ")
            count += 1
            if count == 10:
                count = 1
        print()
    

print_answer(n)