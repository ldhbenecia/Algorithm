def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []
    
    # 할인율 [10, 10] ~ [40, 40]
    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        
        for i in data:
            temp[depth] += i
            dfs(temp, depth + 1)
            temp[depth] -= i
    dfs([0] * len(emoticons), 0)
    
    for i in range(len(discount)):
        join, price = 0, [0] * len(users)
        for j in range(len(emoticons)):
            for k in range(len(users)):
                # 할인율이 더 높으면 무조건 구매
                if users[k][0] <= discount[i][j]:
                    price[k] += emoticons[j] * (100 - discount[i][j]) / 100
        
        # 가입자(join) 갱신
        for k in range(len(users)):
            if price[k] >= users[k][1]:
                join += 1
                price[k] = 0
        
        # 최대 가입자, 금액 갱신
        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)
            answer[0] = join
    
    return answer
