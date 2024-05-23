import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  nums = list(map(int, input().split()))
  
  # 팀의 인원이 6명인지 체크 후 제거
  test_team_number = set(nums)
  for i in test_team_number:
    if nums.count(i) < 6:
      while i in nums:
        nums.remove(i)
 
  result_dic = {}
  index_dict = {i: [] for i in nums}
  
  # index_dict = key: 팀 번호, values: 등수 
  for idx, team in enumerate(nums):
    index_dict[team].append(idx + 1)
  
  # dic = key: 팀 번호, values: 등수 합계
  for team, score in index_dict.items():
    result_dic[team] = (sum(score[:4]), score[4])
  
  # 1등 팀 결정 (score가 적을 수록 순위 높음)
  min_score = float('inf')
  min_team = None
  min_fifth_score = float('inf')
  
  for team, (sum_score, fifth_score) in result_dic.items():
    if sum_score < min_score or (sum_score == min_score and fifth_score < min_fifth_score):
      min_score = sum_score
      min_fifth_score = fifth_score
      min_team = team
    
  print(min_team)