n =  int(input())

cnt = 0
six_end = 666

while True:
    if '666' in str(six_end):
        cnt += 1
    if cnt == n:
        print(six_end)
        break
    six_end += 1