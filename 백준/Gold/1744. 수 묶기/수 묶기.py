n = int(input())

plus = []
minus = []
result = 0

for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    # 0도 음수를 제거하기 위한 수단으로 minus에 삽입
    elif num <= 0:
        minus.append(num)
    # 1이 있으면 처음부터 합산
    else:
        result += num

plus.sort(reverse=True)
minus.sort()

# 양수 처리
for i in range(0, len(plus) - 1, 2):
    result += plus[i] * plus[i + 1]
if len(plus) % 2 != 0:
    result += plus[-1]

# 음수
for i in range(0, len(minus) - 1, 2):
    result += minus[i] * minus[i + 1]
if len(minus) % 2 != 0:
    result += minus[-1]

print(result)

# 정리
# 1. 1은 무조건 묶지 말고 더해야 한다.
# 2. 양수와 음수를 분리한다.
# 3. 양수는 내림차순으로 정렬해서 곱하면 큰 값이다.
# 4. 음수는 오름차순으로 정렬해서 곱하면 큰 값이다.
