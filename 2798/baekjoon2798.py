n, m = map(int,input().split())
card = list(map(int,input().split()))

card_sum = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i] + card[j] + card[k] <= m:
                card_sum.append(card[i] + card[j] + card[k])

print(max(card_sum))


'''
n, m = map(int,input().split())
card = list(map(int,input().split()))

card_sum = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                card_sum = max(card_sum, card[i] + card[j] + card[k])

print(card_sum)
'''