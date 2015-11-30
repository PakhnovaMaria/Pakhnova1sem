class Matrix:
    def __init__(self, m, n=None):
        if isinstance(m, int):
            if not isinstance(n, int): raise ValueError()
            if n<=0 or m<=0: raise ValueError()
            self.m = m
            self.n = n
            self.Matr = [[0] * n for i in range(m)]
        elif not isinstance(m, list): raise ValueError()
        else:
            if len(m) == 0: raise ValueError()
            if n!= None: raise ValueError()
            self.Matr = m
            self.m = len(m)
            self.n = len(m[0])

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError()

        body = [[None]*self.n for i in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                body[i][j] = self.Matr[i][j] + other.Matr[i][j]
        return Matrix(body)

    def __eq__(self, other):
        if self.m != other.m or self.n != other.n: raise RuntimeError()
        for i in range(self.m):
            for j in range(self.n):
                if self.Matr[i][j] != other.Matr[i][j]:
                    return False
            return True

    def __sub__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError()

        body = [[None]*self.n for i in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                body[i][j] = self.Matr[i][j] - other.Matr[i][j]
        return Matrix(body)

    def get(self, i, j):
        return self.Matr[i][j]

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def set(self, i, j, value):
        self.Matr[i][j] = value

    def get_size(self):
        A = (self.m, self.n)
        return A

    def transpose(self):
        body = [[None]*self.m for i in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                body[j][i] = self.Matr[i][j]
        return Matrix(body)

    def __mul__(self, other):
        if type(other) in [int, float]:
             body = [[None]*self.n for i in range(self.m)]
             for i in range(self.m):
                for j in range(self.n):
                    body[i][j] = self.Matr[i][j] * other
        elif type(other) != Matrix: raise RuntimeError()
        else:
            if self.n != other.m: raise RuntimeError()
            body = [[None]*other.n for i in range(self.m)]
            for i in range(self.m):
                for j in range(other.n):
                    body[i][j] = 0
                    for k in range(self.n):
                        body[i][j] += self.Matr[i][k]*other.Matr[k][j]
        return Matrix(body)


    def __truediv__(self, other):
        if type(other) in [int, float]:
            return self * (1/other)



    def determinant(self):
        pass

    def __str__(self):
        return str(self.Matr)






