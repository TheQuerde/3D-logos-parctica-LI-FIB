from vpython import *
#import numpy as np
import math

class Turtle3D():
    def __init__(self):
        # paràmetres de l'escena
        scene.height = scene.width = 1000
        scene.autocenter = True
        scene.caption = """\nTo rotate "camera", drag with right button or Ctrl-drag.\nTo zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.\n  On a two-button mouse, middle is left + right.\nTo pan left/right and up/down, Shift-drag.\nTouch screen: pinch/extend to zoom, swipe or two-finger rotate.\n"""
        self.bola = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.green, make_trail=True, interval=5, trail_radius=0.5)
        self.bola.velocity = vector(0,1,0)

    def hide(self):
        self.bola.make_trail=False

    def show(self):
        self.bola.make_trail=True

    def home(self):
        self.bola.pos = vector(0,0,0)
        self.bola.velocity = vector(0,1,0)

    def color(self, r, g, b):
        self.bola.color = vector(r,g,b)
        self.bola.trail_color = vector(r,g,b) 
        
    def forward (self, size):
        i = 0
        while i <= size:
            self.bola.pos += self.bola.velocity*i 
            i += .1
            rate(100)
 
    def backward (self, size):
        i=0
        while i <= size:
            self.bola.pos -= self.bola.velocity*i
            i -= .1
            rate(100)

    def left(self, a):
        v2 =self.bola.velocity.rotate(angle=radians(a), axis=vector(0,0,1))
        self.bola.velocity = v2

    def right(self, a):
        v2 =self.bola.velocity.rotate(angle=radians(a), axis=vector(0,0,-1))
        self.bola.velocity = v2

    def up(self, a):
        v2 =self.bola.velocity.rotate(angle=radians(a),axis=vector(1,0,0))
        self.bola.velocity = v2

    def down(self, a):
        v2 =self.bola.velocity.rotate(angle=radians(a),axis=vector(-1,0,0))
        self.bola.velocity = v2

