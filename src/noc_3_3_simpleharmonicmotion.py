# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-3: Simple Harmonic Motion
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/NOC_3_05_simple_harmonic_motion
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=21
# Migrated to py5

import py5


def setup():
    py5.size(640, 360)


def draw():
    py5.background(255)

    period = 120    # number of frames for one full oscillation cycle
    amplitude = 300 # max displacement from center

    # x = A * sin(2π * t / T) — standard SHM formula using frame count as time
    x = amplitude * py5.sin(py5.TWO_PI * py5.frame_count / period)

    py5.stroke(0)
    py5.stroke_weight(2)
    py5.fill(127)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.line(0, 0, x, 0)
    py5.ellipse(x, 0, 48, 48)

if __name__ == "__main__":
    py5.run_sketch()
