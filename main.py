"""This will approximate lens shape for aspheric lens to focus on single point"""


from lenses import Lens
from light import Light
from display import Display

focalLenght = 1000
lensWidth = 500
n1 = 1.0
n2 = 1.5


"""Create lens1 """
lens1 = Lens(focalLenght, lensWidth, n1, n2)
lens1.lowerApproximation()

surface1 = lens1.surface
print(f"surface1 = {surface1}")


"""Set number of light sources"""
numberLightRays = 22
"""Initiate Class Light"""
light = []  #Light List for light objects

""" Create instances of light"""
for i in range(numberLightRays): #
    light.append(Light(i, lens1))

""" LIGHT SOURCE POINTS IN LIGHT OBJECTS """
for lightBeam in light:
    lightBeam.lightSource()

for lightBeam in light:
    lightBeam.rayLensIntersection(Lens)




#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_Lens1(surface1)

for lightBeam in light:
    toScreen.draw_Source(lightBeam.ray[0])

toScreen.display_to_screen()