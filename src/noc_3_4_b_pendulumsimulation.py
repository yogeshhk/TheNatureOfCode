# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-4 b: Pendulum Simulation
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/NOC_3_10_PendulumExample
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=22
# Migrated to py5

# Pendulum
#
# A simple pendulum simulation
# Given a pendulum with an angle theta (0 being the pendulum at rest) and
# a radius r we can use sine to calculate the angular component of the
# gravitational force.
#
# Gravity Force = Mass * Gravitational Constant;
# Pendulum Force = Gravity Force * sine(theta)
# Angular Acceleration =
#       Pendulum Force / Mass = gravitational acceleration * sine(theta);
#
# Note this is an ideal world scenario with no tension in the pendulum arm,
# a more realistic formula might be:
#       Angular Acceleration = (g / R) * sine(theta)
#
# For a more substantial explanation, visit:
# http://www.myphysicslab.com/pendulum1.html

import py5


class Pendulum(object):
    """
    A Simple Pendulum Class
    Includes functionality for user can click and drag the pendulum
    """

    def __init__(self, origin, r):
        self.position = py5.Py5Vector(0, 0)
        self.origin = py5.Py5Vector(origin.x, origin.y)
        self.r = r
        self.angle = py5.PI / 4
        self.aVelocity = 0.0
        self.aAcceleration = 0.0
        self.ballr = 48
        self.damping = 0.995
        self.dragging = False

    def go(self):
        self.update()
        self.drag()
        self.display()

    def update(self):
        if not self.dragging:
            gravity = 0.4
            # Angular acceleration from pendulum physics: a = -(g/r) * sin(theta)
            self.aAcceleration = (-1 * gravity / self.r) * py5.sin(self.angle)
            self.aVelocity += self.aAcceleration
            self.aVelocity *= self.damping
            self.angle += self.aVelocity

    def display(self):
        # Convert polar angle to Cartesian bob position
        self.position = py5.Py5Vector(
            self.r * py5.sin(self.angle),
            self.r * py5.cos(self.angle)
        )
        self.position += self.origin

        py5.stroke(0)
        py5.stroke_weight(2)
        py5.line(self.origin.x, self.origin.y, self.position.x, self.position.y)
        py5.ellipse_mode(py5.CENTER)
        py5.fill(175)
        if self.dragging:
            py5.fill(0)
        py5.ellipse(self.position.x, self.position.y, self.ballr, self.ballr)

    def clicked(self, mx, my):
        d = py5.dist(mx, my, self.position.x, self.position.y)
        if d < self.ballr:
            self.dragging = True

    def stopDragging(self):
        self.aVelocity = 0
        self.dragging = False

    def drag(self):
        if self.dragging:
            diff = self.origin - py5.Py5Vector(py5.mouse_x, py5.mouse_y)
            # atan2 gives angle from positive x-axis; subtract 90° to get angle from vertical
            angle = py5.atan2(-1 * diff.y, diff.x) - py5.radians(90)
            # Fixed: was computing angle but never assigning it to self.angle
            self.angle = angle


def setup():
    py5.size(640, 360)
    global p
    p = Pendulum(py5.Py5Vector(py5.width / 2, 0), 175)


def draw():
    py5.background(255)
    p.go()


def mouse_pressed():
    p.clicked(py5.mouse_x, py5.mouse_y)


def mouse_released():
    p.stopDragging()

if __name__ == "__main__":
    py5.run_sketch()
