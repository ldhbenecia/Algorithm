n = int(input())

for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)

"""
for i in range(1, n+1):
    print(" " * (n-i), "*" * i) 
#print함수의 특징 중 콤마(,)로 문자열을 나열할 경우 공백이 자동으로 추가되어 콤마를 사용하면 오답.
"""