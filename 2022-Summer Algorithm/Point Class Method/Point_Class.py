'''
class Point:
  def __init__(self, x = 0, y = 0):
    self.x = x # x-좌표를 위한 멤버 self.x
    self.y = y # y-좌표를 위한 멤버 self.y
    
p = Point(1, 2)
print(p) # <__main__.Point object at 0x7f420a277fd0>
# __str__ 함수가 정의되어 있지 않기 때문에 print함수가 무엇을 출력해야하는 지 알 수 없음
# 고로 저 메세지 출력

class Point2:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    
  def __str__(self):
    return f"({self.x}, {self.y})"
	
p = Point2(1, 2)		# x = 1, y = 2인 객체 생성
print(p)			# p.__str__()이 호출되고, 리턴된 "(1, 2)"를 출력함
s = str(p) # p.__str__()형식으로 호출
print(s) # (1, 2)
'''


class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f"({self.x}, {self.y})"
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)
  def __rmul__(self, other):
    return Point(self.x * other, self.y * other)
	
p = Point(1, 2)
q = Point(3, 4)
r = p - q
print(r) # (-2, -2)
r = 3 * p
print(r) # (3, 6)
r = p * 3		# 이 문장은 에러를 발생시킨다!
print(r)


class Vector:
  def __init__(self, *args):
    self._coords = list(args) #[x for x in args]

  def __str__(self):
    return str(self._coords)
    
  def __len__(self): # return its dimension
    return len(self._coords)

  def __getitem__(self, k): # return the value of kth dimension
    return self._coords[k]
    
  def __setitem__(self, k, val): # return the value of kth dimension
    self._coords[k] = val

v = Vector(1, 2, 3)
v[-1] = 9

for c in v:
    print(c, end=" ")
print() # 1 2 9