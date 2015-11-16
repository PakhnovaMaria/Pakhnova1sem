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
    def abs(a):
        #print((self.x ** 2 + self.y ** 2) ** 0.5)
        return (a.x ** 2 + a.y ** 2) ** 0.5
    def perimeter (a,b,c):
         #print(a,b,c,Point.abs(a-b)+ Point.abs(b-c) + Point.abs(c-a))
         return Point.abs(a-b)+ Point.abs(b-c) + Point.abs(c-a)

N = int(input())
p = [Point(input().replace(' ', ',')) for i in range(N)]
Max = 0
a, b, c = p[:3]
for i in p:
    for j in p:
        for k in p:
            per = Point.perimeter(i, j, k)/2
            S = (per * (per - Point.abs(i-j)) * (per - Point.abs(i-k)) * (per - Point.abs(j-k))) ** (0.5)
            if S > Max:
                a, b, c = i, j, k
                Max = S
print(Max)