n, m = map(int, input().split())
word = list(input() for _ in range(n))

# m보다 짧은 단어 소거
word = [w for w in word if len(w) >= m]

# 단어당 빈도수 체킹을 위한 딕셔너리
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

result = []

# 1. 빈도수가 높은 단어 우선 정렬
# 2. 빈도수가 같다면 단어가 긴 것 우선 정렬
# 3. 빈도수와 길이가 같다면, 알파벳순 정렬
freq_sort = sorted(dic.keys(), key=lambda x: (-dic[x], -len(x), x)) # 내림차순 -, 오름차순 +

for i in range(len(freq_sort)):
    result.append(freq_sort[i])

for i in result:
    print(i)
