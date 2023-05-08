n = int(input())
num_list = set(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

for i in check_list:
  if i in num_list:
    print(1)
  else:
    print(0)