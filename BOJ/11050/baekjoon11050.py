'''
import math

n, k = map(int, input().split())
bino = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(bino)
'''

n, k = map(int, input().split())

def fac(a):
    if a == 0:
        return 1
    if a == 1:
        return 1
    else:
        return a * fac(a-1)
    
print(fac(n) // (fac(n-k) * fac(k)))