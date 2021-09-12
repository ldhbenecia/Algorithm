# a = 고정 비용, b = 가변 비용, c = 노트북 가격
a, b, c = map(int,input().split())

a/(c-b)+1
if b >= c:
    print("-1")
else:
    print(a//(c-b)+1) #+1을 해주는 이유는 +1을 했을 때부터 최초 이익이 발생하는 손익분기점이기 때문