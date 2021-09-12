n = int(input())
result = 0

for i in range(1, n+1):
    arr = list(map(int,str(i))) # 각 자릿수로 나누기 2/1/6
    result = i + sum(arr) # 분해합 = 생성자 + 각 자릿수의 합
    if result == n: # 처음 분해합과 입력값이 같을 때가 가장 작은 생성자를 가질 때
        print(i)
        break
    
    if i == n: #생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)