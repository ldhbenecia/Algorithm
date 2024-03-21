def solution(genres, plays):
    answer = []
    
    dic = {}
    dic_count = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in dic.keys():
            dic[genre] += [(i, play)]  # (인덱스, 재생횟수)
            dic_count[genre] += play
        else:
            dic[genre] = [(i, play)] # (인덱스, 재생횟수)
            dic_count[genre] = play
            
    sorted_dic = sorted(dic_count.items(), key= lambda i:i[1], reverse=True)
    sorted_genres = [genre for genre, _ in sorted_dic]
    
    for genre, plays in sorted_dic:
        print(genre, plays, dic[genre])
        sorted_song = sorted(dic[genre], key= lambda x:x[1], reverse=True) # 재생횟수 순서로 정렬
        for idx, plays in sorted_song[:2]:
            answer.append(idx)
            
    return answer
