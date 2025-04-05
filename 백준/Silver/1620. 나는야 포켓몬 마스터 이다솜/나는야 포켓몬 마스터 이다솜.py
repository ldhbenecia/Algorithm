n, m = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, n + 1):
    name = input().strip()

    name_to_num[name] = i
    num_to_name[str(i)] = name

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(num_to_name[q])
    else:
        print(name_to_num[q])
