# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example I-5: Perlin Noise
# PyP5 port by: Yogesh Kulkarni
# Updated by : Akanksha Suneri
# Migrated to py5
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/introduction/NOC_I_5_NoiseWalk
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=6

import py5
import random

class Walker(object):

    def __init__(self):
        self.location = py5.Py5Vector(py5.width / 2, py5.height / 2)
        self.noff = py5.Py5Vector(random.random(), random.random())

    def display(self):
        py5.stroke_weight(2)
        py5.fill(127)
        py5.stroke(0)
        py5.ellipse(self.location.x, self.location.y, 48, 48)

    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        self.location.x = int(py5.noise(float(self.noff.x)) * py5.width) #map(noise(self.noff.x), 0, 1, 0, width)
        self.location.y = int(py5.noise(float(self.noff.y)) * py5.height)  #map(noise(self.noff.y), 0, 1, 0, height)
        self.noff = self.noff + py5.Py5Vector(0.01, 0.01)


def setup():
    py5.size(800, 200)
    # frameRate(30) # Not Implemnted in p5py

    # Create a walker object
    global w
    w = Walker()


def draw():
    py5.background(255)
    # Run the walker object
    w.walk()
    w.display()

if __name__ == "__main__":
    py5.run_sketch()