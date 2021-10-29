n, k = map(int,input().split())
measure = []

for i in range(1,n+1):
    if n % i == 0:
        measure.append(i)

if k > len(measure):
    print(0)
else:
    print(measure[k-1])