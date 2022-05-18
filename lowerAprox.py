import math

"""This class will calculate positions of lens surface to make a lens that focuses light at a single point."""

class Outside():
    def __init__(self, focalLength, lensWidth, n1, n2):
        self.d = focalLength
        self.lensTop = lensWidth/2
        self.n1 = n1
        self.n2 = n2
        self.theta1 = 0.0
        self.theta2 = 0.0
        self.lensCoords = [0.0, 0.0]
        self.lensAngle = math.pi/2


    def buildLens(self):

        for i in range(round(self.lensTop)):
            thetaRay = math.atan(i / self.d)
            self.theta1 = math.atan((-1.5 * math.sin(thetaRay)) / (1 - 1.5 * math.cos(thetaRay)))
            self.theta2 = math.asin(math.sin(self.theta1)/ self.n2)
            #sum = thetaRay + self.theta2
            dy = self.d * math.tan(thetaRay)
            self.lensCoords[1] += dy


            print(f"theta1, theta2, thetaRay = {self.theta1*180/math.pi,self.theta2*180/math.pi, thetaRay*180/math.pi}")

            thetaN = self.theta1 + math.pi / 2



