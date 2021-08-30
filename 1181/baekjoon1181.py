n = int(input())

word = []

for i in range(n):
    word.append(i)
    word.sort(key=len)
    print(word[i])
