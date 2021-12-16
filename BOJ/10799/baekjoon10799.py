bar = input()

stack = []
count = 0

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
        
    else: # ')' 가 나왔을 때
        if bar[i-1] == '(': # '()'가 된다면
            stack.pop() # 막대기가 아니라 레이저이므로 
            count += len(stack)
        else: # '))' 
            stack.pop()
            count += 1
            
print(count)

'''
bar = list(map(str, input()))

stack = []
count = 0

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append('(')
        
    elif bar[i-1] == ')':
        stack.pop()
        count += 1
    
    else:
        stack.pop()
        count += len(stack)

print(count)
'''