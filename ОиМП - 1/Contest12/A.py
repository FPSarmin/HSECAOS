from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, mat):
        self.mat = deepcopy(mat)
        self.n = len(self.mat)
        self.m = len(self.mat[0])

    def __str__(self):
        strMat = ''
        for i in self.mat:
            strMat += '\t'.join(map(str, i)) + '\n'
        return strMat[:-1]

    def size(self):
        return self.n, self.m

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise MatrixError(self, other)
        sumMat = deepcopy(self)
        for i in range(self.n):
            for j in range(self.m):
                sumMat.mat[i][j] += other.mat[i][j]
        return sumMat

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            mulMat = deepcopy(self)
            for i in range(self.n):
                for j in range(self.m):
                    mulMat.mat[i][j] *= other
            return mulMat
        else:
            if self.m != other.n:
                raise MatrixError(self, other)
            mulMat = [[0 for j in range(other.m)]
                      for i in range(self.n)]
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        mulMat[i][j] += self.mat[i][k] * other.mat[k][j]

            return Matrix(mulMat)

    __rmul__ = __mul__

    def transpose(self):
        trans = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                trans[j][i] = self.mat[i][j]
        self.mat = trans
        self.n, self.m = self.m, self.n
        return self

    def transposed(self):
        trans = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                trans[j][i] = self.mat[i][j]
        return Matrix(trans)

    def strDiv(self, b, k, l):
        for i in range(self.m):
            self.mat[k][i] /= l
        b[k] /= l

    def strSwap(self, b, k, l):
        self.mat[k], self.mat[l] = self.mat[l], self.mat[k]
        b[k], b[l] = b[l], b[k]

    def strSum(self, b, k, l, m):
        for i in range(self.m):
            self.mat[k][i] += self.mat[l][i] * m
        b[k] += b[l] * m

    def solve(self, b):
        x = deepcopy(self)
        column = 0
        while column < len(b):
            currM = None
            for i in range(column, x.n):
                if currM is None or\
                        abs(x.mat[i][column] > abs(x.mat[currM][column])):
                    currM = i
            if currM is None:
                raise MatrixError(x, b)
            if currM != column:
                x.strSwap(b, currM, column)
            x.strDiv(b, column, x.mat[column][column])
            for i in range(column + 1, x.n):
                x.strSum(b, i, column, -x.mat[i][column])
            column += 1
        answer = [0] * len(b)
        for i in range(len(b) - 1, -1, -1):
            answer[i] = b[i] - sum(c*a for c, a in
                                   zip(answer[(i+1):], x.mat[i][(i+1):]))
        return answer


class SquareMatrix(Matrix):
    def __pow__(self, power, modulo=None):
        if power == 0:
            eMat = Matrix([[0 for i in range(self.n)]
                           for j in range(self.m)])
            for i in range(self.n):
                for j in range(self.m):
                    if i == j:
                        eMat.mat[i][j] = 1
            return eMat
        if power % 2 == 0:
            tempMat = deepcopy(self)
            tempMat = tempMat ** (power // 2)
            return tempMat * tempMat
        if power % 2 == 1:
            tempMat = deepcopy(self)
            tempMat = tempMat ** (power - 1)
            return tempMat * self


exec(stdin.read())
