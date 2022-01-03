data = input()
row = int(data[1])
column = int(ord(data[0]) - int(ord('a')) + 1) #입력 값의 영어를 숫자로 변환
count = 0

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

for i in steps:
    location_row = row + i[0]
    location_column = column + i[1]
    
    if location_row >= 1 and location_row <= 8 and location_column >= 1 and location_column <= 8:
        count += 1
        
print(count)