# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-4 a: Pendulum Simulation
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/??
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=22
# Migrated to py5

import py5


def setup():
    global origin, bob, angle, length, aVel, aAcc
    py5.size(640, 360)
    length = 180
    angle = py5.PI / 4
    aVel = 0.0
    aAcc = 0.0

    origin = py5.Py5Vector(py5.width / 2, 0)
    bob = py5.Py5Vector(py5.width / 2, length)


def draw():
    py5.background(255)
    global origin, bob, angle, length, aVel, aAcc

    bob.x = origin.x + length * py5.sin(angle)
    bob.y = origin.y + length * py5.cos(angle)
    py5.line(origin.x, origin.y, bob.x, bob.y)
    py5.ellipse(bob.x, bob.y, 48, 48)

    # Angular acceleration: a = -(g_factor) * sin(theta)
    aAcc = -0.01 * py5.sin(angle)

    angle += aVel
    aVel += aAcc
    aVel *= 0.99  # slight damping so the pendulum eventually comes to rest

if __name__ == "__main__":
    py5.run_sketch()
