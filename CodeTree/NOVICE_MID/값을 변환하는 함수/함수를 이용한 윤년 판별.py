y = int(input())

def leap_year(n):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    if y % 400 == 0:
        return True
    return False
    
if leap_year(y):
    print("true")
else:
    print("false")