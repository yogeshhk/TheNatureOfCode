# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 2-5: Drag Force
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp02_forces/NOC_2_5_fluidresistance
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=17
# Migrated to py5

import py5
import random

class Mover(object):
    def __init__(self, m, x, y):
        self.position = py5.Py5Vector(x, y)
        self.velocity = py5.Py5Vector(0, 0)
        self.acceleration = py5.Py5Vector(0, 0)
        self.mass = m

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

class Liquid(object):
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def contains(self, m):
        l = m.position
        return (l.x > self.x) and (l.x < (self.x + self.w)) and \
                (l.y > self.y) and (l.y < (self.y + self.h))

    def drag(self, m):
        """
        Calculates the drag force: F_drag = -c * v^2 in the direction opposing motion
        """
        speed = m.velocity.mag
        dragMagnitude = self.c * speed * speed

        dragForce = py5.Py5Vector(m.velocity.x, m.velocity.y)
        dragForce *= -1
        dragForce.normalize()
        dragForce *= dragMagnitude
        return dragForce

    def display(self):
        py5.no_stroke()
        py5.fill(50)
        py5.rect(self.x, self.y, self.w, self.h)

def setup():
    py5.size(640, 360)
    reset()

    global liquid
    liquid = Liquid(0, py5.height / 2, py5.width, py5.height / 2, 0.1)

def draw():
    py5.background(255)

    liquid.display()

    for mover in movers:
        if liquid.contains(mover):
            dragForce = liquid.drag(mover)
            mover.applyForce(dragForce)

        gravity = py5.Py5Vector(0, 0.1 * mover.mass)
        mover.applyForce(gravity)

        mover.update()
        mover.display()
        mover.checkEdges()

def mouse_pressed():
    reset()

def reset():
    global movers
    movers = [Mover(random.uniform(0.5, 3), 40 + i * 70, 0) for i in range(8)]

if __name__ == "__main__":
    py5.run_sketch()
