# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example I-1: Random Walker
# PyP5 port by: Yogesh Kulkarni
# Updated by : Akanksha Suneri
# Migrated to py5 
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/tree/master/introduction/NOC_I_1_RandomWalkTraditional
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=2

import py5
import random


class Walker(object):

    def __init__(self):
        self.x = py5.width / 2
        self.y = py5.height / 2

    def render(self):
        py5.stroke(0)
        py5.point(float(self.x), float(self.y))

    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        choice = int(random.randint(0,3))

        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1

        self.x = py5.constrain(self.x, 0, py5.width - 1)
        self.y = py5.constrain(self.y, 0, py5.height - 1)

def setup():
    py5.size(640, 360)
    # Create a walker object
    global w
    w = Walker()
    py5.background(255)

def draw():
    # Run the walker object
    w.step()
    w.render()

if __name__ == "__main__":
    py5.run_sketch()