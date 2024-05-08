def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2), 
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
     
    use_left = [1, 4, 7]
    use_right = [3, 6, 9]
    use_close = [2, 5, 8, 0]
    
    current_left = '*'
    current_right = '#'
    
    for num in numbers:
        if num in use_left:
            answer += 'L'
            current_left = num
        
        elif num in use_right:
            answer += 'R'
            current_right = num
        
        else:
            target_x, target_y = keypad[num]
            left_x, left_y = keypad[current_left]
            right_x, right_y = keypad[current_right]
            
            left_distance = distance(target_x, target_y, left_x, left_y)
            right_distance = distance(target_x, target_y, right_x, right_y)
            
            if left_distance < right_distance:
                answer += 'L'
                current_left = num
                
            elif left_distance > right_distance:
                answer += 'R'
                current_right = num
                
            else: 
                if hand == 'left':
                    answer += 'L'
                    current_left = num
                else:
                    answer += 'R'
                    current_right = num
        
    return answer