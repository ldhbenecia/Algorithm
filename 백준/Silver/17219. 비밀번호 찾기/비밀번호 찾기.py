n, m = map(int, input().split())

save = {}

# n개 만큼의 사이트 주소와 비밀번호 입력
for i in range(n):
  domain, password = input().split()
  save[domain] = password
  
find = []

# m개 만큼의 비밀번호를 찾으려는 사이트 주소 입력
for j in range(m):
  find_domain = input()
  find.append(find_domain)
  
# 딕셔너리에서 해당하는 키 값이 있으면 그에 해당하는 밸류 값 출력
for i in find:
  if save.get(i):
    print(save.get(i))