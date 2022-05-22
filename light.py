import math

from linearAlg import LinAlg


class Light():
    """Light class for Light objects"""
    def __init__(self, rayNumber, lens):   #Number of rays to be generated
        self.rayNumber = rayNumber
        self.rayX0 = -300   # X position of light source
        self.rayY0 = 0    # Y position of light source
        self.rayX1 = -50
        self.rayY1 = 0
        self.sourceWidth = 10   # Vertical distance between rays
        self.ray = []           # ray position
        self.angle = []          # ray angle
        self.lens = lens
        self.lensSegment = []

        #self.lens = lens  # Initiate Lens Class This will depend on the type of lens being used
        #self.lens2 = SecondLens()
        #self.xfp = 0   # The points where the ray crosses the focal line

    def lightSource(self):
        """ SOURCE POINTS """
        self.ray.append([self.rayX0, self.rayY0 + self.rayNumber * self.sourceWidth])
        self.ray.append([self.rayX1, self.rayY1 + self.rayNumber * self.sourceWidth])
        self.angle.append(0)
        return self.ray

    def rayLensIntersection(self, lens):
        """Use cramers rule to find intersection of
        ray line and lens line """
        rX1, rY1 = self.ray[-2][0], self.ray[-2][1]
        rX2, rY2 = self.ray[-1][0], self.ray[-1][1]
        lineR =  [[rY1,rY1],[rX2, rY2]]
        #print(f"rX1, rY1 = {rX1, rY1} rX2, rY2 = {rX2, rY2}")

        for i in range(1, len(self.lens)):
            lX1, lY1 = self.lens[i-1][0], self.lens[i-1][1]
            lX2, lY2 = self.lens[i][0], self.lens[i][1]
            lineL = [[lX1, lY1],[lX2, lY2]]

            point = LinAlg.line_intersection(lineR, lineL)
            if point[0] >= lX1 and point[0] <= lX2:
                if point[1] >= lY1 and point[1] <= lY2:
                    #print(f"point = {point}")
                    self.ray.append([point[0], point[1]])
                    self.lensSegment = lineL
                    #print(f"lenSegment = {self.lensSegment}")
                    slope = (lY2-lY1)/(lX2-lX1)
                    normAngle = math.atan(slope) - math.pi/2
                    print(f"normAngle = {normAngle * 180 / math.pi}")
                    print(f"Nslope = {math.tan(normAngle)}")
                    print(f"slope = {slope}")
                    print(-1/slope)

    def refraction(self, n1, n2):
        """Ray -Lens1 refraction."""
        # Compute Normal Vector




