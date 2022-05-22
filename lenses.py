import math

"""This class will calculate positions of lens surface to make a lens that focuses light at a single point."""

class Lens():
    def __init__(self, focalLength, lensWidth, n1, n2):
        self.d = 0 - focalLength
        self.lensTop = lensWidth/2
        self.n1 = n1
        self.n2 = n2
        self.theta1 = 0.0
        self.theta2 = 0.0
        self.surface = [[100.0, 0.0]]
        self.lensAngle = math.pi/2
        self.unitNormalVector = []


    def lowerApproximation(self):
        """Approximate lens"""
        xR, yR = 1000, 0
        n = 300
        dy = self.lensTop/n
        print(f"round(self.lensTop) = {round(self.lensTop)}")
        for i in range(1, n):
            y = i * dy
            thetaRay = math.atan(y / self.d)
            self.theta1 = math.atan((-self.n2 * math.sin(thetaRay)) / (1 - self.n2 * math.cos(thetaRay)))
            self.theta2 = math.asin(math.sin(self.theta1)/ self.n2)
            #sum = thetaRay + self.theta2
            self.lensAngle = math.pi/2 + self.theta1
            mL = math.tan(self.lensAngle)
            mR = math.tan(thetaRay)
            xL = self.surface[i-1][0]
            yL = self.surface[i-1][1]
            x = (mL*xL - yL - mR*xR + yR) / (mL - mR)
            y = mR*(x - xR) + yR
            self.surface.append([x, y])


            lensSlope = math.tan(self.lensAngle)


            #print(f"theta1, theta2, thetaRay lensAngle, lensSlope, x, y = {self.theta1*180/math.pi,self.theta2*180/math.pi, thetaRay*180/math.pi, self.lensAngle*180/math.pi, lensSlope, x, y}")

            thetaN = self.theta1 - math.pi / 2
            x = math.cos(thetaN)
            y = math.sin(thetaN)
            self.unitNormalVector = [x, y]



