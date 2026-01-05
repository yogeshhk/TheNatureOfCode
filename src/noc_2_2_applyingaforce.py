# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 2-2: Applying a force?
# PyP5 port by: Yogesh Kulkarni
# Updated by : Akanksha Suneri
# Migrated to py5
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp02_forces/NOC_2_1_forces
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=14

import py5

class Mover(object):
    def __init__(self):
        self.position = py5.Py5Vector2D(30, 30)
        self.velocity = py5.Py5Vector2D(0, 0)
        self.acceleration = py5.Py5Vector2D(0, 0)

    def applyForce(self, force):
        self.acceleration += force

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def display(self):
        py5.stroke(0)
        py5.stroke_weight(2)
        py5.fill(127)
        py5.ellipse(self.position.x, self.position.y, 48, 48)

    def checkEdges(self):
        if (self.position.x > py5.width):
            self.position.x = py5.width
            self.velocity.x *= -1
        elif (self.position.x < 0):
            self.position.x = 0
            self.velocity.x *= -1

        if (self.position.y > py5.height):
            self.position.y = py5.height
            self.velocity.y *= -1


def setup():
    py5.size(640, 360)
    global m
    m = Mover()


def draw():
    py5.background(255)

    gravity = py5.Py5Vector2D(0, 0.1)
    m.applyForce(gravity)

    if py5.is_mouse_pressed:
        wind = py5.Py5Vector2D(0.01, 0)
        m.applyForce(wind)

    m.update()
    m.display()
    m.checkEdges()


if __name__ == "__main__":
    py5.run_sketch()