n = int(input())
con = []

for _ in range(n):
    start, end = map(int, input().split())
    con.append([start, end])
    
con.sort(key = lambda x: (x[0])) # 시작 시간 기준 오름차순
con.sort(key = lambda x: (x[1])) # 끝나는 시간으로 다시 오름차순

last_time = 0 # 마지막 시간 저장할 변수
count = 0 # 회의 개수

for i, j in con:
    if i >= last_time: # 시작시간이 회의의 마지막 시간보다 크거나 같은 경우
        count += 1
        last_time = j
        
print(count)