n = 1000 - int(input())
change = [500, 100, 50, 10, 5, 1]
count = 0

for i in change:
    count += n // i
    n %= i
    
print(count)