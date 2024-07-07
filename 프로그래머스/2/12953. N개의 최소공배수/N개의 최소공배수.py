def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(arr):
    n = arr[0]
    
    for i in range(1, len(arr)):
        gcd = get_gcd(n, arr[i])
        n = n * arr[i] // gcd
    
    return n