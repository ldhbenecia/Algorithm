t = int(input())

for _ in range(t):
    qus = list(input())
    score = 0
    sum_score = 0
    
    for i in qus:
        if i == "O":
            score += 1
            sum_score += score
        else:
            score = 0

    print(sum_score)