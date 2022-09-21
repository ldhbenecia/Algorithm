def reverse(A):
  if len(A) == 1:
    return A
  return reverse(A[1:] + A[0]) # A[0]를 맨 뒤로 보내고 나머지는 재귀
# O(n^2_)


def reverse2(A, start, stop): # stop-1까지가 대상임에 유의
  if start < stop -1: # 2개 이상의 값이 있는 경우만 의미 있으므로
    A[start], A[stop-1] = A[stop-1], A[start]
    reverse(A, start+1, stop-1)
# O(n)