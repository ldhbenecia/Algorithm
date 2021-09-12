n = int(input())

word = []

for i in range(n):
    word.append(input())

set_word = list(set(word)) # 중복 단어 제거
sort_word = []

for i in set_word:
    sort_word.append((len(i), i)) # 단어의 길이, 단어 함께 저장

sort_word.sort() # 오름차 순 정렬

for i, j in sort_word: # i = 단어의 길이, j = 단어
    print(j) # j를 출력하면 단어, i를 출력하면 단어의 길이 값이 출력됨