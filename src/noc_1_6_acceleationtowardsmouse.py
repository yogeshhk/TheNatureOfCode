# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 1-6: Acceleration towards mouse
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp01_vectors/NOC_1_7_motion101
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=12
# Migrated to py5

import py5

class Mover(object):

    def __init__(self):
        self.location = py5.Py5Vector(py5.width / 2, py5.height / 2)
        self.velocity = py5.Py5Vector(0, 0)
        self.acceleration = py5.Py5Vector(0, 0)

    def update(self):
        # Vector from mover to mouse, normalized to a tiny constant acceleration
        mouse = py5.Py5Vector(py5.mouse_x, py5.mouse_y)
        mouse -= self.location
        mouse.magnitude = 0.1

        self.acceleration = mouse
        self.velocity += self.acceleration
        self.location += self.velocity
        # Limit speed to 5
        self.velocity.set_limit(5)

    def display(self):
        py5.stroke(0)
        py5.stroke_weight(2)
        py5.fill(127)
        py5.ellipse(self.location.x, self.location.y, 48, 48)

    def checkEdges(self):
        if self.location.x > py5.width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = py5.width

        if self.location.y > py5.height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = py5.height

def setup():
    py5.size(640, 360)
    global mover
    mover = Mover()


def draw():
    py5.background(255)
    mover.update()
    mover.checkEdges()
    mover.display()

if __name__ == "__main__":
    py5.run_sketch()
