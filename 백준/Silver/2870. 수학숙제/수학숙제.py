n = int(input())
result = []

for _ in range(n):
    content = input()
    temp = ""
    for i in content:
        if i.isdigit():
            temp += i
        # 문자가 나올 경우
        else:
            # 숫자가 차있으면, 숫자 등록하고 정리
            if temp != "":
                result.append(int(temp))
                temp = ""

    # 문자가 나와서 정리가 안되는 경우
    if temp != "":
        result.append(int(temp))

result.sort()
for i in result:
    print(i)
