n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 만들어진 graph의 총 금 개수 파악
def get_gold(row_s, col_s, row_e, col_e):
    gold = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            gold += graph[row][col]

    return gold


result = 0

for row in range(n):
    for col in range(n):
        # 3*3 격자가 튀어나가면 안됨. in_range() 생각
        if row + 2 >= n or col + 2 >= n:
            continue
        
        gold = get_gold(row, col, row + 2, col + 2)

        result = max(result, gold)

print(result)