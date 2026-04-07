# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-2: Trigonometry and Polar Coordinates
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/NOC_3_04_PolarToCartesian
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=20
# Migrated to py5

import py5


# PolarToCartesian
# Convert a polar coordinate (r,theta) to cartesian (x,y):
# x = r * cos(theta)
# y = r * sin(theta)


def setup():
    py5.size(640, 360)
    global r, theta, angularVelocity, angularAcceleration
    r = py5.height * 0.45
    theta = 0
    angularVelocity = 0.0
    angularAcceleration = 0.01


def draw():
    py5.background(255)
    global r, theta, angularVelocity, angularAcceleration

    py5.translate(py5.width / 2, py5.height / 2)

    x = r * py5.cos(theta)
    y = r * py5.sin(theta)

    py5.ellipse_mode(py5.CENTER)
    py5.fill(127)
    py5.stroke(0)
    py5.stroke_weight(2)
    py5.line(0, 0, x, y)
    py5.ellipse(x, y, 48, 48)

    theta += angularVelocity
    angularVelocity += angularAcceleration
    angularVelocity = py5.constrain(angularVelocity, 0, 0.1)

if __name__ == "__main__":
    py5.run_sketch()
