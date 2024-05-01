def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n % m)

def lcm(n, m):
    return (n * m) // gcd(n, m)

def solution(n, m):
    answer = []
    
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    
    return answer