t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    count = 0
    wonder = [0 for i in range(n)]
    wonder[m] = 1 # 0으로만 이루어진 리스트에 1을 넣어 궁금한 문서 중요도 값이 제일 크게 해둠
    
    while importance:
        if importance[0] == max(importance):
            count += 1 # 인쇄해서 인쇄한 개수 1 추가
            
            if wonder[0] == 1:
                print(count)
                break
            else:
                importance.pop(0)
                wonder.pop(0)
        else:
            importance.append(importance[0])
            wonder.append(wonder[0])
            importance.pop(0)
            wonder.pop(0)