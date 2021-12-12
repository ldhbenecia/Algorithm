n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]
    
answer = []
temp = k-1

for i in range(n):
    if len(lst) > temp:
        answer.append(lst.pop(temp))
        temp += k-1
    elif len(lst) <= temp:
        temp = temp % len(lst)
        answer.append(lst.pop(temp))
        temp += k-1
        
print("<", ', '.join(str(i) for i in answer), ">", sep = '')