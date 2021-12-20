h = []

for _ in range(9):
    h.append(int(input()))

sum_total = sum(h)

for i in range(8):
    for j in range(i+1, 9):
        if sum_total - (h[i] + h[j]) == 100:
            one = h[i]
            two = h[j]
            
h.remove(one)
h.remove(two)
h.sort()

for i in h:
    print(i)