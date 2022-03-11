#!/usr/bin/env python

import prman
import math

ri = prman.Ri()

filename = "__render"  # "perfume.rib"
ri.Begin(filename)

ri.Display("perfume.exr", "it", "rgba")
ri.Format(720, 576, 1)
# ri.Format(1920, 1080, 1)
# ri.Projection(ri.ORTHOGRAPHIC)
ri.Projection(ri.PERSPECTIVE,{ri.FOV:100})

ri.WorldBegin()
# ri.Scale(0.1,0.1,0.1)
ri.Translate(0, 0, 10)
# ri.Rotate(-65, 1, 0, 0)

bodyHeight = 6.7
bodyRadius = 1.65
capHeight = 2.8
capRadius = 0.95
middleHeight = 1.3

### Body ###
ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Cylinder(bodyRadius, -bodyHeight, 0, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
a = bodyRadius
b = capRadius
h = middleHeight
d = (a*a-b*b-h*h)/(2*h)
r = math.sqrt(((a-b)*(a-b)+h*h)*((a+b)*(a+b)+h*h)/(4*h*h))
ri.Translate(0, 0, -d)
ri.Sphere(r, d, h+d, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Translate(0, 0, -bodyHeight)
minorRadius = 0.3
degree = -135
ri.Torus(bodyRadius-minorRadius, minorRadius, degree, 0, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
height = -bodyHeight+math.sin(math.radians(degree))*minorRadius
radius = bodyRadius-minorRadius+math.sin(math.radians(degree))*minorRadius
ri.Disk(height, radius, 360)
ri.TransformEnd()

### Cap ###
ri.TransformBegin()
ri.Translate(0, middleHeight, 0)
ri.Rotate(-90, 1, 0, 0)
ri.Cylinder(capRadius, 0, capHeight, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Translate(0, 0, middleHeight+capHeight)
minorRadius = 0.05
ri.Torus(capRadius-minorRadius, minorRadius, 0, 90, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Disk(middleHeight+capHeight+minorRadius, capRadius-minorRadius, 360)
ri.TransformEnd()

ri.WorldEnd()
ri.End()