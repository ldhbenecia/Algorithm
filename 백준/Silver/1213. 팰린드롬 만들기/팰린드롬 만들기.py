from collections import Counter

name = sorted(list(input()))
word = Counter(name)

odd = 0
odd_alphabet = ''
result = ''
for i in word:
    if word[i] % 2 != 0:
        odd += 1
        odd_alphabet += i
    
        if odd >= 2:
            print("I'm Sorry Hansoo")
            exit()

for i in word:
    result += i * (word[i] // 2)
    
print(result + odd_alphabet + result[::-1])
