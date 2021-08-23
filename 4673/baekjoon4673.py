#전체 자연수 - 생성자가 있는 숫자 = 셀프 넘버

numbers = set(range(1,10000)) #전체 자연수
remove_num = set() #생성자가 있는 숫자

for i in range(1,10001): #1부터 10000까지 반복
    for j in str(i): #1부터 10000까지 반복한 숫자를 문자로 하나하나 나누어 j로 저장
        i += int(j) #1부터 10000까지 숫자가 들어가는데 하나 하나씩 나누어진 숫자를 정수형으로 더하기
    remove_num.add(i) #이 숫자들은 생성자가 있는 숫자

self_numbers = numbers - remove_num #셀프 넘버

for i in self_numbers:
    print(i)