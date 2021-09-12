#한수 = 각 자리가 등차수열을 이루는 것

n = int(input())
hansu = 0

for i in range(1, n+1):
    if i < 100:
        hansu += 1
    else:
        numbers = list(map(int, str(i)))
        if numbers[0] - numbers[1] == numbers[1] - numbers[2]:
            hansu += 1

print(hansu)