#!/usr/bin/env python

import prman

ri = prman.Ri()

filename = "__render"  # "perfume.rib"
ri.Begin(filename)

ri.Display("perfume.exr", "it", "rgba")
ri.Format(720, 576, 1)
# ri.Format(1920, 1080, 1)
ri.Projection(ri.PERSPECTIVE,{ri.FOV:100})

ri.WorldBegin()

ri.Translate(0, 0, 10)
# ri.Rotate(-25, 1, 0, 0)

### Body ###
ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Cylinder(1.65, -6.7, 0, 360)
ri.Translate(0, 0, -0.05)
ri.Sphere(1.650757402, 0.05, 1.35, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Translate(0, 0, -6.7)
ri.Torus(1.35, 0.3, -135, 0,360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Disk(-6.92, 1.14, 360)
ri.TransformEnd()

### Cap ###
ri.TransformBegin()
ri.Translate(0, 1.3, 0)
ri.Rotate(-90, 1, 0, 0)
ri.Cylinder(0.95, 0, 2.8, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Translate(0, 0, 4.1)
ri.Torus(0.9, 0.05, 0, 90, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Disk(4.15, 0.9, 360)
ri.TransformEnd()

ri.WorldEnd()
ri.End()