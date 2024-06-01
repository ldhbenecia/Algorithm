n = int(input())
position = sorted(list(map(int, input().split())))

mid = (n - 1) // 2
print(position[mid])


""" 1 2 3 4 5 100 101이 주어질 경우 안됨
n = int(input())
position = sorted(list(map(int, input().split())))

average = sum(position) // n

stack = []
for i in position:
  stack.append((abs(average - i), i))

stack.sort()
home = stack[0][1]

print(home)

"""
