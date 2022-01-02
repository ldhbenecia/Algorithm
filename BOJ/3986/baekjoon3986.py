n = int(input())
count = 0

for _ in range(n):
    word = input()
    stack = []
    
    for i in word:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack) == 0:
        count += 1
        
print(count)