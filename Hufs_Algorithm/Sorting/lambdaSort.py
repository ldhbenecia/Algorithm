S = [(1, 2), (4, 5), (4, -3)]
S.sort(key=lambda x: x[1])
print(S) #[(4, -3), (1, 2), (4, 5)]

S.sort(key=lambda x: x[0]+x[1])
print(S) #[(4, -3), (1, 2), (4, 5)]

S.sort(key=lambda x: x[0]-x[1])
print(S) #[(1, 2), (4, 5), (4, -3)]
