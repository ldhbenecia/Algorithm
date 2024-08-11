n = int(input())
task = [input() for _ in range(n)]

result = []
for i in task:
    num = ''
    for j in i:
        if j.isnumeric():
            num += j
        else:
            if num:
                result.append(num)
                num = ''
    if num:
        result.append(num)

result = list(map(int, result))
result.sort()     
for i in result:
    print(i)
