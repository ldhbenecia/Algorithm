n = int(input())
pattern = input().split("*")

left = pattern[0]
right = pattern[1]

for _ in range(n):
    name = input()

    if name.startswith(left) and name.endswith(right) and len(name) >= len(left) + len(right):
        print("DA")
    else:
        print("NE")
