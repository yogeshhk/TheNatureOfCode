# Reference : https://p5.readthedocs.io/en/latest/install.html
# Prerequisite: https://www.glfw.org/download.html for Windows

# Migrated to https://py5coding.org/index.html
# Installation Instructions : https://py5coding.org/content/install.html
# Updated by : Akanksha Suneri
# Details : Updated file to latest py5 syntax 
# A simple py5 sketch to test installation

import py5

def setup():
    py5.size(200, 200)

def draw():
    py5.rect_mode(py5.CENTER)
    py5.rect(100, 100, 20, 100)
    py5.ellipse(100, 70, 60, 60)
    py5.ellipse(81, 70, 16, 32)
    py5.ellipse(119, 70, 16, 32)
    py5.line(90, 150, 80, 160)
    py5.line(110, 150, 120, 160)

if __name__ == "__main__":
    py5.run_sketch()