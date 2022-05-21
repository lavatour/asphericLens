import math
from lenses import Lens
from linearAlg import LinAlg


class Light():
    """Light class for Light objects"""
    def __init__(self, rayNumber, lens):   #Number of rays to be generated
        self.rayNumber = rayNumber
        self.sourceX = 0   # X position of light source
        self.sourceY = 0    # Y position of light source
        self.sourceWidth = 10   # Vertical distance between rays
        self.ray = []           # ray position
        self.angle = []          # ray angle
        self.lens = lens
        #self.lens = lens  # Initiate Lens Class This will depend on the type of lens being used
        #self.lens2 = SecondLens()
        #self.xfp = 0   # The points where the ray crosses the focal line

    def lightSource(self):
        """ SOURCE POINTS """
        self.ray.append([self.sourceX, self.sourceY + self.rayNumber * self.sourceWidth])
        self.angle.append(0)
        return self.ray

    def rayLensIntersection(self, lens):
        """Derive equation for ray"""


        """Derive equation for lens segment"""
        """Loop through lens segments"""
        mR = math.tan(self.angle[-1])
        xR = self.ray[-1][0]
        yR = self.ray[-1][1]


        for i in range(len(self.lens.surface) - 1):
            #print(f"i = {i}")
            xL, yL = self.lens.surface[i][0], self.lens.surface[i][1]
            xl2, yl2 = self.lens.surface[i+1][0], self.lens.surface[i+1][1]
            mL = LinAlg.slope(self, xL, yL, xl2, yl2)
            bL = -mL*xL + yL
            #print(f"bl = {bL}")
            #print(f"self.lens.surface[i] = {self.lens.surface[i]}")
            x = (mR*xR - mL*xL - yR + yL) / (mR - mL)
            print(f"mL = {mL}")
            y = mL*x + bL
            print(f"y = {y}")
            if y > self.lens.surface[i][1]:
                print(f"i = {i}")
                print(f"self.lens.surface[i] = {self.lens.surface[i]}")
                print(f"x, y = {x,y}")
                break


            #print(f"ray = {self.ray}")
            y = self.ray[-1][1]
            #print(f"y = {y}")
            #print(f"rayAngle = {self.angle}")















            #mL = LinAlg.slope()

