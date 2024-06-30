def solution(n, k, cmd):
    answer = ['O'] * n
    linked_lst = {i: [i - 1, i + 1] for i in range(n)}
    delete_lst = []
    
    for command in cmd:
        command = command.split()
        
        if command[0] == 'D':
            for _ in range(int(command[1])):
                k = linked_lst[k][1]
        elif command[0] == 'U':
            for _ in range(int(command[1])):
                k = linked_lst[k][0]
        
        elif command[0] == 'C':
            prev, nxt = linked_lst[k]
            answer[k] = 'X' # 제거
            delete_lst.append((prev, k, nxt))
            
            # 마지막 행인 경우
            if nxt == n:
                k = linked_lst[k][0] # 바로 윗 행 선택
            else:
                k = linked_lst[k][1] # 바로 아래 행 선택
            
            if prev == -1:
                linked_lst[nxt][0] = prev
            elif nxt == n:
                linked_lst[prev][1] = nxt
            else:
                linked_lst[prev][1] = nxt
                linked_lst[nxt][0] = prev

        else:
            prev, now, nxt = delete_lst.pop()
            answer[now] = 'O' # 복구
            
            if prev == -1:
                linked_lst[nxt][0] = now
            elif nxt == n:
                linked_lst[prev][1] = now
            else:
                linked_lst[prev][1] = now
                linked_lst[nxt][0] = now
            
    return ''.join(answer)