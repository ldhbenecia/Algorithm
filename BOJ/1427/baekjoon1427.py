lst = list(map(int, input()))
lst.sort(reverse=True)

for i in lst:
    print(i, end='')