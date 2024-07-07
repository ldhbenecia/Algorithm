import math

def solution(arr):
    n = arr[0]
    
    for i in range(1, len(arr)):
        gcd = math.gcd(n, arr[i])
        n = n * arr[i] // gcd
    
    return n