def measure_count(num):
    count = 0

    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            if i == num // i:
                count += 1
            else:
                count += 2
            
    return count

def solution(number, limit, power):
    answer = 0
    measure_counts = []
                            
    for i in range(1, number + 1):
        measure = measure_count(i)
        measure_counts.append(measure)

    for measure in measure_counts:
        if measure <= limit:
            answer += measure
        elif measure > limit:
            answer += power

    return answer