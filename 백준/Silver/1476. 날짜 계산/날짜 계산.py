e, s, m = map(int, input().split())
result = 0
E, S, M = 0, 0, 0

while True:
    E += 1
    S += 1
    M += 1
    result += 1
    
    if E == e and S == s and M == m:
        break

    if E == 15:
        E = 0
    if S == 28:
        S = 0
    if M == 19:
        M = 0

print(result)
