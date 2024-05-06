def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    correct = 0
    zero_count = lottos.count(0)
    
    for num in lottos:
        if num in win_nums:
            correct += 1
            
    best = correct + zero_count
    worst = correct
        
    return [rank[best], rank[worst]]
