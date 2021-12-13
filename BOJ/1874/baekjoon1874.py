n = int(input())

stack = []
answer = []
count = 1
impossible = 0

for _ in range(n):
    num = int(input())
    
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1
        
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        impossible = 1
        break
    
if impossible == 0:
    for i in answer:
        print(i)