n = int(input())
word_list = [input() for _ in range(n)]
dic = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0,
}

# 입력한 숫자에 따른 자릿수 배정
for i in word_list:
  for j in range(len(i)):
    num = 10 ** (len(i) - j - 1) 
    dic[i[j]] += num

words = sorted(dic.values(), reverse=True)
result = 0
n = 9
for i in words:
  result += i * n
  n -= 1
  
print(result)
