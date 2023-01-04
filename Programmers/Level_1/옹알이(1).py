from itertools import permutations

def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for i in babbling:
        for j in word:
            i = i.replace(j,"*", 1)
        if i.replace("*", "") == "":
            cnt += 1
            
    return cnt
  