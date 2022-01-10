n, m = map(int, input().split())

dic = {}

for i in range(1, n+1): # 포켓몬 입력
    data = input()
    # 숫자 또는 문자로 맞춰야할 문제가 나오므로
    # 딕셔너리에 번호와 이름을 둘 다 저장
    dic[i] = data
    dic[data] = i
    
for i in range(m):
    problem = input()
    # isdigit() 함수는 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
    
    if problem.isdigit() == True: # 맞춰야할 문제가 숫자로만 이루어져있을 시
        print(dic[int(problem)]) # 딕셔너리의 그 숫자 포켓몬 이름 출력
        # dic[int(problem)] -> dic[Pikachu] = 피카츄 번호 
    else: # 맞춰야할 문제가 포켓몬 이름으로 이루어져있을 시
        print(dic[problem]) # 딕셔너리의 그 포켓몬 이름 숫자 출력
        # dic[problem] -> dic[12] = 12번째 포켓몬