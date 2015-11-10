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

a = Point(input())
print(a)


