#!/usr/bin/env python3
import math

def triangle(base, height):
  return base * height/2

def rectangle(base, height):
  return base * height

def circle(radius):
  return math.pi * (radius**2)


area_of_circle = circle(4)
print(area_of_circle)
