"""This will approximate lens shape for aspheric lens to focus on single point"""


from lenses import Lens
from light import Light
from display import Display

focalLength = 1000
lensWidth = 1000
n1 = 1.0
n2 = 1.5
scale = 0.25

"""Create lens1 """
lens1 = Lens(focalLength, lensWidth, n1, n2)
lens1.lowerApproximation()

surface1 = lens1.surface
print(f"surface1 = {surface1}")

"""Create lens2"""
lens2 = Lens(focalLength, lensWidth, n2, n1)
lens2.secondLens(lens1, scale)
surface2 = lens2.secondLens(lens1, scale)
print(f"25 surface2 = {surface2}")

"""Set number of light sources"""
numberLightRays = 34
"""Initiate Class Light"""
light = []  #Light List for light objects

""" Create instances of light"""
for i in range(numberLightRays): #
    light.append(Light(i, surface1))

""" LIGHT SOURCE POINTS IN LIGHT OBJECTS """
for lightBeam in light:
    lightBeam.lightSource()

for lightBeam in light:
    lightBeam.rayLensIntersection(lens1)

""" LIGHT LENS1 REFRACTION"""
for lightBeam in light:
    lightBeam.refraction(n1, n2)


for lightBeam in light:
    lightBeam.rayExtension()
#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_Lens1(surface1)
print(f"surface1 = {surface1}")
toScreen.draw_Lens1(surface2)
print(f"surface2** = {surface2}")


for lightBeam in light:
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()