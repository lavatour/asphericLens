import math
import numpy as np

class LinAlg:
    def __init__(self):
        pass

    def dotProd(self, A, B):
        B = np.transpose(B)
        A = np.array(A)
        B = np.array(B)
        dotProd = np.dot(A, B)
        return dotProd

    def crossProd(self, A, B):
        crossProd = np.cross(A, B)
        return crossProd

    def scalarMultiplication(self, scalar, A):
        """Multiply a matrix by a scalar"""
        for i in range(len(A)):
            A[i] = -1 * A[i]
        return A

    def makeUnitVector(self, x1, y1, x2, y2):
        x = x2-x1
        y = y2-y1
        length = math.sqrt(x**2 + y**2)
        ux = x / length
        uy = y / length
        unitVecter = [ux, uy]
        return unitVecter

    def slope(self, x1, y1, x2, y2):
        if x2 == x1:
            return 1000000
        m = (y2 - y1) / (x2 - x1)
        return  m

    def Y_Intercept(self, x1, y1, x2, y2):
        """y = y1 = m(x - x1)
        x = 0 at y intercept
        y = -mx1 + y1"""
        m = (y2 - y1) / (y2 - y1)
        yInt = -m*x1 + y1

    def standardForm(self, x1, y1, x2, y2):
        m = (y2 - y1) / (y2 - y1)
        A = m
        B = -1
        C = m*x1 + y1
        return (A, B, C)

    def adjointMatrix(self, M):
        A= [[0, 0], [0, 0]]
        A[0][0] = M[1][1]
        A[0][1] = -M[1][0]
        A[1][1] = M[0][0]
        A[1][0] = -M[0][1]
        return A

    def determinant(self, M):
        d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        return d

    def scalarMultiplication(self, scalar, A):
        """Multiply a matrix by a scalar"""
        #if type(A) == list:
        B = np.asarray(A) * scalar
        s = scalar
        #print(f"s = {s}")
        #B = s * A
        return B

    def inverse2X2(self, M):
        d = LinAlg.determinant(self, M)
        A = LinAlg.adjointMatrix(self, M)
        I = LinAlg.scalarMultiplication(self, 1/d, M)
        return I

    def line_intersection(line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y

