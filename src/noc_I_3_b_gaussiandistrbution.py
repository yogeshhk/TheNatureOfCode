# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example I-3-b: Gaussian Distribution
# PyP5 port by: Yogesh Kulkarni
# Updated by : Akanksha Suneri
# Migrated to py5
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/introduction/NOC_I_4_Gaussian
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=4

import py5

def setup():
    py5.size(640, 360)
    py5.background(255)


def draw():
    # Get a gaussian random number w/ mean of 0 and standard deviation of 1.0
    xloc = py5.random_gaussian()
    sd = 60  # Define a standard deviation
    # Define a mean value (middle of the screen along the x-axis)
    mean = py5.width / 2
    # Scale the gaussian random number by standard deviation and mean
    xloc = (xloc * sd) + mean
    py5.fill(0, 10)
    py5.no_stroke()
    # Draw an ellipse at our "normal" random location
    py5.ellipse(xloc, py5.height / 2, 16, 16)

if __name__ == "__main__":
    py5.run_sketch()