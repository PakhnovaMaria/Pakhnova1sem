class Point:
    def new(x, y):
        return Point(str(x)+','+str(y))
    def __init__ (self, descr='0,0'):
        self.x,  self.y = [float(i) for i in descr.split(',')]
    def __add__ (self, other):
        return Point.new(self.x + other.x, self.y + other. y)
    def __sub__ (self, other):
        return Point.new(self.x - other.x, self.y - other. y)
    def __eq__ (self, other):
        return self. x == other. x and self.y == other.y
    def  __str__ (self):
        return str(self.x) + ',' + str(self.y)
    def __abs__ (self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def perimeter (a,b,c):
         return abs(a-b)+ abs(b-c) + abs(c-a)

N = int(input())
p = [Point(input().replace(' ', ',')) for i in range(N)]
per = 0
a, b, c = p[:3]
for i in p:
    for j in p:
        for k in p:
            if Point.perimeter(i, j, k) > per:
                per = Point.perimeter(i, j, k)
                a, b, c = i, j, k
print(per)
