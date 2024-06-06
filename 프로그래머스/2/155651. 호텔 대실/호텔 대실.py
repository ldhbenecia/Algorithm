import heapq

def change(time):
    hours, minutes = time.split(':')
    return 60 * int(hours) + int(minutes)

def solution(book_time):
    rooms = []
    book_time.sort()
    
    for i in book_time:
        check_in = change(i[0])
        check_out = change(i[1]) + 10
        
        if rooms and rooms[0] <= check_in:
            heapq.heappop(rooms)
        heapq.heappush(rooms, check_out)
        
    return len(rooms)