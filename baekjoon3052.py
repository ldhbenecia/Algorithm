result = []

for _ in range(10):
    a = int(input())
    mod = a % 42
    result.append(mod)

set_result = set(result)
print(len(set_result))