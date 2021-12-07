n = int(input())

result = 0

for i in range(n+1): #시
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k):
                result += 1
                
print(result)