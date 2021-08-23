a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
mul_str = str(mul)

for i in range(10):
    num_count = mul_str.count(str(i))
    print(num_count)