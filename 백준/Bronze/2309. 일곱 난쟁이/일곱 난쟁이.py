heights = []

for _ in range(9):
    heights.append(int(input()))
    
heights.sort(reverse=True)
sum_height = sum(heights)

flag = False

for i in range(9):
    for j in range(9):
        if sum_height - heights[i] - heights[j] == 100:
            remove1 = heights[i]
            remove2 = heights[j]

            if remove1 != remove2:
                heights.remove(remove1)
                heights.remove(remove2)
                flag = True
            break
    
    if flag:
        break
    
heights.sort()            
for i in heights:
    print(i)