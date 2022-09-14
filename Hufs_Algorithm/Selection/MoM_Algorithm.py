def find_median_five(L):
  # L의 다섯 개 이하의 값 중에서 중간값을 찾아 리턴하는 코드 작성
  # 5개의 그룹으로 나누었을 때 이곳에서의 중간값 중에서 중간값을 구해야 함
  
  length = len(L) # 리스트 길이
  median = int(length / 2) # 리스트 길이의 중간에 위치하는 값이 중간값일 것
  
  # 예를 들어 정렬된 7개의 값이 있으면 7/2 = 3해서 L[3]에 중간값이 있는 것
  # 이 경우 length = 7, median = 3 
  
  if length % 2 == 1: # 주어진 리스트의 길이가 홀수일 경우, length 7 % 2 == 1
    return L[median] # 중간값, L[3]에 위치하는 값이 정렬된 기준 중간값
  
  else: # 홀수가 아닐 경우, length 8일 경우
    # 리스트 안에 8개의 요소가 있을 경우 중간값은 L[3], L[4] 두개의 사이 값
    # median = 8 / 2 = 4
    return int((L[median - 1] + L[median]) / 2) # L[3] + L[4] / 2
	
def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
  if len(L) == 1: # no more recursion
    return L[0]
  i = 0
  A, M, B, medians = [], [], [], []
  while i+4 < len(L):
    medians.append(find_median_five(L[i: i+5]))
    i += 5
    
  if i < len(L) and i+4 >= len(L): # 마지막 그룹으로 5개 미만의 값으로 구성
    medians.append(find_median_five(L[i:]))
    
  mom = MoM(medians, len(medians)//2)
  for v in L:
    if v < mom:
      A.append(v)
    elif v > mom:
      B.append(v)
    else:
      M.append(v)
      
  if len(A) >= k : 
    return MoM(A, k)
  elif len(A) + len(M) < k: 
    return MoM(B, k - (len(A) + len(M)))
  else:
    return mom

# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
n, k = map(int, input().split())
L = list(map(int, input().split()))
print(MoM(L, k))