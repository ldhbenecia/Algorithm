n, k = map(int, input().split()) # 응시자 수, 상을 받는 사람 수
x = list(map(int, input().split())) # 학생 점수 리스트
x.sort(reverse=True)

print(x[k-1])