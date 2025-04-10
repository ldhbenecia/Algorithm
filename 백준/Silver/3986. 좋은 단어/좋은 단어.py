n = int(input())
words = [input() for _ in range(n)]

result = 0
for word in words:
    temp = []
    for i in word:
        if not temp:
            temp.append(i)
        else:
            if i == temp[-1]:
                temp.pop()
            else:
                temp.append(i)

    if len(temp) == 0:
        result += 1

print(result)
