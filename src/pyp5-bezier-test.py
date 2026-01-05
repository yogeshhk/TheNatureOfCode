# Reference : https://github.com/p5py/p5/issues/199

import py5

def setup():
    py5.size(200, 200)

def draw():
    py5.background(204)
    py5.bezier(85, 20, 10, 10, 90, 90, 15, 80)
if __name__ == "__main__":
    py5.run_sketch()