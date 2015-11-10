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
    def __perimetr (a,b,c):
        return (abs(a-b) + abs(b-c) + abs(c-a))

N = int(input())
for i in range(N):
    p = Point(input())
per = 0
a, b, c = p[:3]
for i in p:
    for j in p:
        for k in p:
            if Point.perimetr(i, k, j) > per:
                per = Point.perimetr(i, k, j)
                a, b, c = i, k, j
print(per)
