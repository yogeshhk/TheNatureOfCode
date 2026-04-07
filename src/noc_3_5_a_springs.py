# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-5a: Springs
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/??
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=22
# Migrated to py5

import py5

class Mover(object):
    def __init__(self, x, y):
        self.position = py5.Py5Vector(x, y)
        self.velocity = py5.Py5Vector(0, 0)
        self.acceleration = py5.Py5Vector(0, 0)
        self.mass = 1

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

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
    global origin, bob, restLength
    # Fixed: moved Vector init into setup() so py5.width/height are available
    origin = py5.Py5Vector(py5.width / 2, 0)
    bob = Mover(py5.width / 2, 240)
    restLength = 200


def draw():
    py5.background(255)
    py5.line(origin.x, origin.y, bob.position.x, bob.position.y)

    spring = bob.position - origin
    currentLength = spring.mag
    spring.normalize()
    k = 0.1
    stretch = currentLength - restLength
    spring *= -1 * k * stretch
    bob.applyForce(spring)

    gravity = py5.Py5Vector(0, 0.1)
    bob.applyForce(gravity)

    wind = py5.Py5Vector(0.1, 0)
    if py5.is_mouse_pressed:
        bob.applyForce(wind)

    bob.update()
    bob.display()

if __name__ == "__main__":
    py5.run_sketch()
