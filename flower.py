#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:46:51 2020
@author: apoorvakanekal

This is a generative art piece specifically intended to be used as a zoom background image.
"""

import turtle,random

turtle.colormode(255)
panel= turtle.Screen()
w=700
h=700
panel.setup(width=w, height=h)
turtle.tracer(0)

bgPalette = ["#C9CBA3","#FFE1A8","#E26D5C","#723D46","#472D30"]
palette = ["#9CF6F6", "#F3C98B", "#DAA588", "#C46D5E", "#F56960"]
turtle.bgcolor(random.choice(bgPalette))


#sunflower like shape
def sunflower(iteration=24):
    turtle.color(random.choice(palette))
    turtle.up()
    turtle.goto(random.randint(-700,-300),random.randint(200,700))
    turtle.down()
    for element in range(iteration):
        turtle.begin_fill()
        turtle.circle(300,70)
        turtle.left(110)
        turtle.circle(300,70)
        turtle.fd(5)
        turtle.left(5)
        turtle.end_fill()
        
 # circle spiro      
def circspiral(iteration=36):
    turtle.color(random.choice(palette))
    turtle.up()
    turtle.goto(random.randint(300,600),random.randint(-500,-300))
    turtle.down()
    for element in range(iteration):
        turtle.circle(100)
        turtle.fd(10)
        turtle.right(10)

for i in range(3):
    sunflower()
    circspiral()


turtle.done()