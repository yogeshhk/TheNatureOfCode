# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 2-6: Gravitational Attraction
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp02_forces/NOC_2_6_attraction
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=18
# Migrated to py5

import py5
import random

class Mover(object):
    def __init__(self):
        self.position = py5.Py5Vector(400, 50)
        self.velocity = py5.Py5Vector(1, 0)
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
        py5.fill(127, 200)
        py5.ellipse(self.position.x, self.position.y, self.mass * 16, self.mass * 16)

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


class Attractor(object):

    def __init__(self):
        self.position = py5.Py5Vector(py5.width / 2, py5.height / 2)
        self.mass = 20
        self.G = 1

        self.dragOffset = py5.Py5Vector(0.0, 0.0)
        self.dragging = False
        self.rollover = False

    def attract(self, m):
        # Direction from mover to attractor
        force = self.position - m.position
        d = force.mag
        # Clamp distance to avoid extreme forces at very close/far range
        d = py5.constrain(d, 5.0, 25.0)
        force.normalize()
        strength = (self.G * self.mass * m.mass) / float(d * d)
        force *= strength
        return force

    def display(self):
        py5.ellipse_mode(py5.CENTER)
        py5.stroke_weight(4)
        py5.stroke(0)
        if self.dragging:
            py5.fill(50)
        elif self.rollover:
            py5.fill(100)
        else:
            py5.fill(175, 200)
        py5.ellipse(self.position.x, self.position.y, self.mass * 2, self.mass * 2)

    def clicked(self, mx, my):
        d = py5.dist(mx, my, self.position.x, self.position.y)
        if d < self.mass:
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my

    def hover(self, mx, my):
        d = py5.dist(mx, my, self.position.x, self.position.y)
        # Fixed: was assigning to local 'rollover' instead of self.rollover
        self.rollover = d < self.mass

    def stopDragging(self):
        self.dragging = False

    def drag(self):
        if self.dragging:
            self.position.x = py5.mouse_x + self.dragOffset.x
            self.position.y = py5.mouse_y + self.dragOffset.y


def setup():
    py5.size(640, 360)
    global m, a
    m = Mover()
    a = Attractor()


def draw():
    py5.background(255)

    force = a.attract(m)
    m.applyForce(force)
    m.update()

    a.drag()
    a.hover(py5.mouse_x, py5.mouse_y)

    a.display()
    m.display()


def mouse_pressed():
    a.clicked(py5.mouse_x, py5.mouse_y)


def mouse_released():
    a.stopDragging()

if __name__ == "__main__":
    py5.run_sketch()
