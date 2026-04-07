# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-1: Angles and Angular Motion
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/NOC_3_02_forces_angular_motion
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=19
# Migrated to py5

import py5
import random

class Mover(object):
    def __init__(self, mass, x, y):
        self.mass = mass
        self.position = py5.Py5Vector(x, y)
        self.velocity = py5.Py5Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = py5.Py5Vector(0, 0)

        self.angle = 0
        self.aVelocity = 0
        self.aAcceleration = 0

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity

        # Angular acceleration driven by horizontal linear acceleration
        self.aAcceleration = self.acceleration.x / 10.0
        self.aVelocity += self.aAcceleration
        self.aVelocity = py5.constrain(self.aVelocity, -0.1, 0.1)
        self.angle += self.aVelocity

        self.acceleration *= 0

    def display(self):
        py5.stroke(0)
        py5.fill(175, 200)
        py5.rect_mode(py5.CENTER)

        py5.push_matrix()
        py5.translate(self.position.x, self.position.y)
        py5.rotate(self.angle)
        py5.rect(0, 0, self.mass * 16, self.mass * 16)
        py5.pop_matrix()


class Attractor(object):
    """A class for a draggable attractive body in our world"""

    def __init__(self, position, mass=20, g=0.4):
        self.position = py5.Py5Vector(position.x, position.y)
        self.mass = mass
        self.g = g

    def attract(self, m):
        force = self.position - m.position
        distance = force.mag
        distance = py5.constrain(distance, 5.0, 25.0)
        force.normalize()
        strength = (self.g * self.mass * m.mass) / (distance * distance)
        force *= strength
        return force

    def display(self):
        py5.stroke(0)
        py5.stroke_weight(2)
        py5.fill(127)
        py5.ellipse(self.position.x, self.position.y, 48, 48)


max_movers = 20


def setup():
    py5.size(640, 360)
    global movers, a

    movers = [Mover(random.uniform(0.1, 2), random.uniform(0, py5.width), random.uniform(0, py5.height))
              for i in range(max_movers)]
    a = Attractor(py5.Py5Vector(py5.width / 2, py5.height / 2))

    py5.background(255)


def draw():
    py5.background(255)
    a.display()

    for mv in movers:
        force = a.attract(mv)
        mv.applyForce(force)
        mv.update()
        mv.display()

if __name__ == "__main__":
    py5.run_sketch()
