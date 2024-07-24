for i in range(3, 0, -1):
    temp = input()
    if temp.isnumeric():
        n = int(temp) + i # 세 개의 문자열 다음 숫자값 추출

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
