t = int(input())

for _ in range(t):
    n = int(input())
    people = []
    count = 1 # 0이 아닌 이유는 1등이 반드시 존재하기 때문 (한 종목이라도 1등은 무조건 뽑힘)
    
    for _ in range(n):
        doc, interview = map(int,input().split())
        people.append([doc, interview])
        
    people.sort() # 크기 순 오름차순 정렬
    min_score = people[0][1] # 첫번째 지원자 등수, 예제로 따지면 3 2
    
    for i in range(1, n):
        if min_score > people[i][1]:
            count += 1
            min_score = people[i][1]
            
    print(count)