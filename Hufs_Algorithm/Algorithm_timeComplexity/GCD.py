def gcd_sub(a, b):
  while b != 0:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a + b
	
def gcd_mod(a, b): # 유클리드 호제법
	while b != 0:
		a, b = b, a % b
	return a
	
def gcd_rec(a, b):
	if b == 0:
		return a
	else:
		return gcd_rec(b, a % b)
	
# a, b를 입력받는다
a, b = map(int,input().split())

# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)
print(x, y, z)