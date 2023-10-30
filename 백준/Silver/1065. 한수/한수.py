def hansu(n):
  hansu_cnt = 0

  for i in range(1, n+1):
    if i < 100:
      hansu_cnt += 1
    else:
       number = list(map(int, str(i)))
       if number[0] - number[1] == number[1] - number[2]:
         hansu_cnt += 1
  return hansu_cnt

n = int(input())
print(hansu(n))
