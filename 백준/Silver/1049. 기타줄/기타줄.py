n, m = map(int, input().split())

package = []
each = []
for _ in range(m):
  a, b = map(int, input().split())
  package.append(a)
  each.append(b)

# 최소 값들만 추출
min_package = min(package)
min_each = min(each)

answer = 0
while n > 0:
  if n >= 6:
    each_price = min_each * 6
    n -= 6
  else:
    each_price = min_each * n
    n -= n
  
  if min_package < each_price:
    answer += min_package
  else:
    answer += each_price
    
print(answer)

# 1. 패키지가 6묶음이므로 낱개로 6개를 산 가격과 패키지 한 묶음의 산 가격을 비교한다.
# 2. 둘 중 더 작은 값을 answer에 더한다.