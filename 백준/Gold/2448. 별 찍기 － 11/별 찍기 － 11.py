n = int(input())
stars = [[' '] * 2 * n for _ in range(n)]

def make_star(i, j, n):
  # n이 3일 때 삼각형 한 덩이 그리기
  if n == 3:
    # 1열
    stars[i][j] = '*'
    # 2열
    stars[i + 1][j - 1] = '*'
    stars[i + 1][j + 1] = '*'
    # 3열
    stars[i + 2][j - 2] = '*'
    stars[i + 2][j - 1] = '*'
    stars[i + 2][j] = '*'
    stars[i + 2][j + 1] = '*'
    stars[i + 2][j + 2] = '*'
  else:
    half_size = n // 2
    make_star(i, j, half_size)
    make_star(i + half_size, j - half_size, half_size)
    make_star(i + half_size, j + half_size, half_size)

make_star(0, n - 1, n)

for star in stars:
  print("".join(star))
