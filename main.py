"""This will calculate lens shape for aspheric lens to focus on single point"""
import lowerAprox
from lowerAprox import Outside

lens = lowerAprox.Outside(1000, 500, 1.0, 1.5)
lens.buildLens()


