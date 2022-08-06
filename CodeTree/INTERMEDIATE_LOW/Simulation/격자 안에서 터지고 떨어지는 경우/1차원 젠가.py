'''
n = int(input())

numbers = [
    int(input())
    for _ in range(n)
]

result = n

# 삭제 함수
def cut_array(start, end):
    global result, numbers
    temp_arr = []

    for i in range(result):
        if i < start or i > end:
            temp_arr.append(numbers[i])
    
    result = len(temp_arr)
    for i in range(result):
        numbers[i] = temp_arr[i]

    
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    cut_array(s - 1, e - 1) # 인덱스가 아니기라 자릿수로 따져서 -1 해줌


print(result)
for i in range(result):
    print(numbers[i])
'''


n = int(input())
numbers = [
  int(input())
  for _ in range(n)
]

s1, e1 = tuple(map(int, input().split()))
s2, e2 = tuple(map(int, input().split()))

del numbers[s1-1: e1]
del numbers[s2-1: e2]

print(len(numbers))
for i in numbers:
  print(i)