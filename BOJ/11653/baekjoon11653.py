n = int(input())
index = 2

while n != 1:
    if n % index == 0:
        print(index)
        n = n / index
    else:
        index += 1