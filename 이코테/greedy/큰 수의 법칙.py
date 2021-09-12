'''
n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)
'''

n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수
count = (m/(k+1)) * k
count += m % (k+1) # m이 (k+1)로 나누어 떨어지지 않을 시 나머지(가장 큰수)가 추가로 더해짐

# m = 총 수가 몇번 더해지는 지에 대한 입력값
# count = 가장 큰 수를 몇번 더하는 지에 대한 횟수
result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second #가장 큰 수 더한 횟수를 뺀 후 두 번째로 큰 수 더하기

print(int(result))