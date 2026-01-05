# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 1-3: Vector Math
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp01_vectors/NOC_1_3_vector_subtraction
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp01_vectors/NOC_1_4_vector_multiplication/
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=9

import py5


def setup():
    py5.size(500, 300)

def draw():
    py5.background(255)
    py5.stroke_weight(2)
    py5.stroke(0)
    py5.no_fill()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.ellipse(0,0,4,4)

    mouse = py5.Py5Vector(py5.mouse_x, py5.mouse_y)
    center = py5.Py5Vector(py5.width / 2, py5.height / 2)
    mouse -= center # mouse.sub(center)
    mouse *= 0.1

    py5.line(0, 0, mouse.x, mouse.y)

if __name__ == "__main__":
    py5.run_sketch()