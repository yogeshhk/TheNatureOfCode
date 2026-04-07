# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-1: Angles and Angular Motion
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/NOC_3_01_angular_motion
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=19
# Migrated to py5

import py5

angle = 0
aVelocity = 0
aAcceleration = 0.0001


def setup():
    py5.size(800, 200)


def draw():
    global angle, aVelocity, aAcceleration

    py5.background(255)

    py5.fill(127)
    py5.stroke(0)

    py5.translate(py5.width / 2, py5.height / 2)
    py5.rect_mode(py5.CENTER)
    py5.rotate(angle)

    py5.stroke(0)
    py5.stroke_weight(2)
    py5.fill(127)

    py5.rect(0, 0, 64, 36)

    angle += aVelocity
    aVelocity += aAcceleration

if __name__ == "__main__":
    py5.run_sketch()
