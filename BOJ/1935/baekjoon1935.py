t = int(input())
s = input()

operand = []
number = []

for _ in range(t):
    number.append(int(input()))
    
for i in s:
    if 'A' <= i <= 'Z': # 피연산자
        operand.append(number[ord(i) - 65]) 
        # operand 리스트에 number에서 1을 넣을때 ord(문자를 아스키로 바꿔주는 함수)
        # 아스키코드 ord(i)는 A의 아스키코드 65 - 65 = 0
        # number의 1을 인덱스 0번째 자리에 넣어주는 것
        # 그러면 A는 1이 할당되게 됨
    else: # 연산자
        b = operand.pop() #뒤에 추가된 숫자 먼저 빼오기
        a = operand.pop()
        if i == '+':
            operand.append(a+b)
        elif i == '-':
            operand.append(a-b)
        elif i == '*':
            operand.append(a*b)
        elif i == '/':
            operand.append(a/b)
            
print(f'{operand[0]:.2f}')