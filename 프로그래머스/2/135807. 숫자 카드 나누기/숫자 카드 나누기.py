import math
from functools import reduce

#각 최대 공약수와 각 상대 리스트의 원소를 나눈 나머지가 모두 0이 아닐 때 A, B 최대 공약수 중 더 큰 값을 반환
def solution(arrayA, arrayB):
    answer = 0
    
    # arrayA, arrayB의 최대공약수 추출
    arrayA_gcd = reduce(math.gcd, arrayA)
    arrayB_gcd = reduce(math.gcd, arrayB)
    
    # arrayA_gcd가 arrayB의 모든 요소를 나눌 수 없는지 확인
    flagA = True
    for i in arrayB:
        if i % arrayA_gcd  == 0:
            flagA = False
            break
    
    # arrayB_gcd가 arrayA의 모든 요소를 나눌 수 없는지 확인
    flagB = True
    for i in arrayA:
        if i % arrayB_gcd == 0:
            flagB = False
            break

    # 양쪽의 최대 공약수 둘 다 조건 충족 - 이 중 큰 것 선택
    if flagA and flagB:
        answer = max(arrayA_gcd, arrayB_gcd)
    # arrayA_gcd가 arrayB의 모든 숫자를 하나도 못 나눴으니 이 값이 양의 정수 a
    elif flagA:
        answer = arrayA_gcd
    # arrayB_gcd가 arrayA의 모든 숫자를 하나도 못 나눴으니 이 값이 양의 정수 a
    elif flagB:
        answer = arrayB_gcd
            
    return answer
