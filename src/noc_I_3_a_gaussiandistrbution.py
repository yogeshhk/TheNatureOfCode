# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example I-3-a: Gaussian Distribution
# PyP5 port by: Yogesh Kulkarni
# Updated by : Akanksha Suneri
# Migrated to py5
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/introduction/NOC_I_2_RandomDistribution
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=4

import py5
import random

randomCounts = [0.0] * 20


def setup():
    py5.size(640, 360)


def draw():
    py5.background(255)

    # Pick a random number and increase the count
    index = int(random.randint(0,len(randomCounts)-1))
    randomCounts[index] += 1

    # Draw a rectangle to graph results
    py5.stroke(0)
    py5.stroke_weight(2)
    py5.fill(127)

    w = py5.width / len(randomCounts)

    for x, r in enumerate(randomCounts):
        py5.rect(x * w, py5.height - r, w - 1, r)

if __name__ == "__main__":
    py5.run_sketch()