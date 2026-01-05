# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 1-2: PVector Class
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp01_vectors/NOC_1_2_bouncingball_vectors
# But made Object Oriented as per video.
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=8

import py5

class Ball(object):

    def __init__(self):
        self.location = py5.Py5Vector(py5.width/2, py5.height/2)
        self.velocity = py5.Py5Vector(2.5, 5)

    def move(self):
        self.location += self.velocity  # location.add(velocity)

    def bounce(self):
        if (self.location.x > py5.width) or (self.location.x < 0):
            self.velocity.x = self.velocity.x * -1
        if (self.location.y > py5.height) or (self.location.y < 0):
            self.velocity.y = self.velocity.y * -1

    def display(self):
        # Display circle at x location
        py5.stroke(0)
        py5.stroke_weight(2)
        py5.fill(175)
        py5.ellipse(self.location.x, self.location.y, 48, 48)

def setup():
    py5.size(400, 300)
    global b
    b = Ball()

def draw():
    py5.background(255)
    b.move()
    b.bounce()
    b.display()

if __name__ == "__main__":
    py5.run_sketch()