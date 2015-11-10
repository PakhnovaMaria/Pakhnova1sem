class Point:
    def __init__ (self, descr='0,0'):
        self.x,  self.y = [float(i) for i in descr.split(',')]
    def __add__ (self, other):
        return Point(str(self.x + other.x, self.y + other. y))
    def __sub__ (self, other):
        return Point(str(self.x - other.x, self.y - other. y))
    def __eq__ (self, other):
        return self. x == other. x and other. y == other.y
    def  __str__ (self):
        return str(self.x) + ',' + str(self.y)
    def __abs__ (self):
        return (self.x ** 2 + self.y ** 2) ** (0.5)


N = int(input())
x,y=0,0
for i in range(N):
    a = Point(input())
    x += a.x
    y += a.y
print((x)/N, (y)/N)
