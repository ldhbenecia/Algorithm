from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True
        

def solution(numbers):
    answer = 0
    nums = []
    
    for i in range(1, len(numbers) + 1):
        nums.append(list(set(map("".join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(nums, [])))))
    
    for i in per:
        if is_prime(i):
            answer += 1
    
    return answer