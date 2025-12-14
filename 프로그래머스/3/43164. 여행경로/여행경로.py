def solution(tickets):
    answer = []
    
    graph = {}
    for a, b in tickets:
        graph.setdefault(a, []).append(b)
        
    for k in graph:
        graph[k].sort(reverse=True)
    
    
    def dfs():
        stack = ["ICN"]
        
        while stack:
            v = stack[-1]
            
            if v in graph and graph[v]:
                stack.append(graph[v].pop())
            else:
                answer.append(stack.pop())
    
    dfs()
    
    return answer[::-1]