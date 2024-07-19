def solution(numbers):
    answer = []
    
    for num in numbers:
        binary_num = '0' + bin(num)[2:]
        idx = binary_num.rfind('0')
        binary_num = list(binary_num)
        
        # 짝수인 경우(끝이 0인 경우) 끝이 1인 경우로 변경
        if num % 2 == 0:
            binary_num[idx] = '1'
            binary_num = ''.join(binary_num)
        # 홀수인 경우(끝이 1인 경우) 가장 오른쪽의 0을 1로 변경 후 그 다음 값을 0으로 변경
        else:
            binary_num[idx] = '1'
            binary_num[idx + 1] = '0'
            
        answer.append(int(''.join(binary_num), 2))
    
    return answer
