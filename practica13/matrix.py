class Matrix:
    def __init__(self, m, n=None):#m - колво строк, n- колво столбцов
        if not isinstance(m, int):
            raise ValueError()
        if m <= 0:
            raise ValueError()
        if n == None:
            M = m
            self.Matr = m
            self.m = len(M)
            self.n = len(M[0])
        if type(m) == int and type(n) == int:
            if n > 0 and m > 0:
                self.m = m
                self.n = n
                self. Matr = [[0] * n for i in range(m)]

    def __add__(self, other):
        if self.m == other.m and self.n == other.n:
            for i in range(self.m):
                for j in range(self.n):
                    self.Matr[i][j] = self.Matr[i][j] + other.Mart[i][j]
                    return self.Matr

    def __eq__(self, other):
        if self.m == other.m and self.n == other.n:
            for i in range(self.m):
                for j in range(self.n):
                    if self.Matr[i][j] != other.Matr[i][j]:
                        return False
                return True

    def __sub__(self, other):
          if self.m == other.m and self.n == other.n:
            for i in range(self.m):
                for j in range(self.n):
                    self.Matr[i][j] = self.Matr[i][j] - other.Mart[i][j]
                    return self.Matr

    def get(self, i, j):
        return self.Matr[i][j]

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def set(self, i, j, value):
        self.Matr[i][j] = value

    def __mul__(self, other):
        if type(other)  == int:
             for i in range(self.m):
                for j in range(self.n):
                    self.Matr[i][j] = self.Matr[i][j] * other
                    return self.Matr
             else:
                 if self.n == other.m:
                     for i in range(self.m):
                         for j in range(other.n):
                             self.Matr[i][j] = self.i*other.j








