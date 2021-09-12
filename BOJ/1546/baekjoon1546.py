n = int(input())
score = list(map(int, input().split()))

max_score = max(score)
fake_score = []

for i in score:
    fake_score.append(i/max(score)*100)

result = sum(fake_score)/n
print(result)