# The Nature of Code - Daniel Shiffman http://natureofcode.com
# Example 3-5b: Springs
# PyP5 port by: Yogesh Kulkarni
# Adopted from processing.py based implementation at:
# https://github.com/nature-of-code/noc-examples-python/blob/master/chp03_oscillation/NOC_3_11_spring
# But followed on screen example
# Reference Youtube Video: https://www.youtube.com/watch?v=rqecAdEGW6I&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK&index=22
# Migrated to py5

import py5


class Bob(object):
    """
    Bob class, just like our regular
    Mover(position, velocity, acceleration, mass)
    """

    def __init__(self, x, y):
        self.position = py5.Py5Vector(x, y)
        self.velocity = py5.Py5Vector(0, 0)
        self.acceleration = py5.Py5Vector(0, 0)

        self.mass = 24

        # Arbitrary damping to simulate friction / drag
        self.damping = 0.98

        # For mouse interaction
        self.dragOffset = py5.Py5Vector(0, 0)
        self.dragging = False

    def update(self):
        """Standard Euler integration"""
        self.velocity += self.acceleration
        self.velocity *= self.damping
        self.position += self.velocity
        self.acceleration *= 0

    def applyForce(self, force):
        # Newton's law: F = M * A
        f = py5.Py5Vector(force.x, force.y)
        f /= self.mass
        self.acceleration += f

    def display(self):
        """Draw the bob"""
        py5.stroke(0)
        py5.stroke_weight(2)
        py5.fill(175)
        if self.dragging:
            py5.fill(50)
        py5.ellipse(self.position.x, self.position.y, self.mass * 2, self.mass * 2)

    def clicked(self, mx, my):
        """Check if we clicked on the bob"""
        d = py5.dist(mx, my, self.position.x, self.position.y)
        if d < self.mass:
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my

    def stopDragging(self):
        self.dragging = False

    def drag(self, mx, my):
        if self.dragging:
            self.position.x = mx + self.dragOffset.x
            self.position.y = my + self.dragOffset.y


class Spring(object):
    """
    Class to describe an anchor point that can connect to Bob objects via a spring.
    Thank you: http://www.myphysicslab.com/spring2d.html
    """

    def __init__(self, x, y, l):
        self.anchor = py5.Py5Vector(x, y)
        self.length = l  # rest length
        self.k = 0.2     # spring constant

    def connect(self, b):
        """Apply Hooke's Law spring force to bob: F = -k * stretch"""
        force = b.position - self.anchor
        d = force.mag
        stretch = d - self.length
        force.normalize()
        force *= -1 * self.k * stretch
        b.applyForce(force)

    def constrainLength(self, b, minlen, maxlen):
        """Constrain the distance between bob and anchor between min and max"""
        direction = b.position - self.anchor
        d = direction.mag

        if d < minlen:
            direction.normalize()
            direction *= minlen
            b.position = self.anchor + direction
            b.velocity *= 0
        elif d > maxlen:
            direction.normalize()
            direction *= maxlen
            b.position = self.anchor + direction
            b.velocity *= 0

    def display(self):
        py5.stroke(0)
        py5.fill(175)
        py5.stroke_weight(2)
        py5.rect_mode(py5.CENTER)
        py5.rect(self.anchor.x, self.anchor.y, 10, 10)

    def displayLine(self, b):
        py5.stroke_weight(2)
        py5.stroke(0)
        py5.line(b.position.x, b.position.y, self.anchor.x, self.anchor.y)


def setup():
    py5.size(640, 360)
    global bob, spring
    spring = Spring(py5.width / 2, 10, 100)
    bob = Bob(py5.width / 2, 100)


def draw():
    py5.background(255)

    gravity = py5.Py5Vector(0, 2)
    bob.applyForce(gravity)

    spring.connect(bob)
    spring.constrainLength(bob, 30, 200)

    bob.update()
    bob.drag(py5.mouse_x, py5.mouse_y)

    spring.displayLine(bob)
    bob.display()
    spring.display()

    py5.fill(0)
    py5.text("click on bob to drag", 10, py5.height - 5)


def mouse_pressed():
    bob.clicked(py5.mouse_x, py5.mouse_y)


def mouse_released():
    bob.stopDragging()

if __name__ == "__main__":
    py5.run_sketch()
