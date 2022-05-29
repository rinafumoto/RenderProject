#!/usr/bin/env python
import perfume

ri = perfume.ri

bodyHeight = 6.7
bodyRadius = 1.65
bottomMinorRadius = 0.3

##### SETTINGS #####
ri.Begin("__render")
ri.Display("perfume.exr", "it", "rgba")
# ri.Format(720, 576, 1)
ri.Format(1920, 1080, 1)

# ri.Hider("raytrace", {
#     "int incremental": [1],
#     "int minsamples": 128,
#     "int maxsamples": 256
# })
# ri.ShadingRate(1)
# ri.PixelVariance(10)
ri.Integrator("PxrPathTracer", "integrator")

ri.Projection(ri.PERSPECTIVE,{ri.FOV:35})
# ri.Projection(ri.PERSPECTIVE,{ri.FOV:40})
# ri.DepthOfField(fstops[i], 0.6, 27)

##### GLOBAL TRANSFORMATION #####

ri.Translate(0, 1.2, 28)


ri.WorldBegin()

perfume.lighting()
perfume.env()

ri.TransformBegin()

ri.Translate(10, bodyRadius-(bodyHeight+bottomMinorRadius), -3)
ri.Rotate(60, 0,1,0)
ri.Rotate(90, 1,0,0)
ri.Rotate(-90, 0,1,0)
perfume.bottle()

ri.TransformEnd()

ri.TransformBegin()

ri.Translate(-10,0,0)
perfume.bottle([0.5,0.5,0.5],[0.3,0.3,0.3])

ri.Translate(5,0,0)
ri.TransformBegin()
ri.Rotate(30, 0,1,0)
perfume.bottle([0.6,0.3,0.4],[0.4,0.2,0.3])
ri.TransformEnd()

ri.Translate(5,0,0)
ri.TransformBegin()
ri.Rotate(30, 0,1,0)
perfume.bottle([0.12,0.18,0.26],[0.08,0.12,0.17])
ri.TransformEnd()

ri.Translate(5,0,0)
ri.TransformBegin()
ri.Rotate(30, 0,1,0)
perfume.bottle([0.1,0.1,0.1],[0.07,0.07,0.07])
ri.TransformEnd()

ri.TransformEnd()

# Silver
# perfume.bottle([0.5,0.5,0.5],[0.5,0.5,0.5])
# perfume.bottle([0.9,0.9,0.9],[0.9,0.9,0.9])
# Rose
# perfume.bottle([0.6,0.3,0.4],[0.6,0.3,0.4])
# perfume.bottle([0.7,0.4,0.5],[0.7,0.4,0.5])
# Navy
# perfume.bottle([0.12,0.18,0.26],[0.12,0.18,0.26])
# Green
# perfume.bottle([0.05,0.09,0.01],[0.05,0.09,0.01])
# Red
# perfume.bottle([0.3,0.03,0.03],[0.3,0.03,0.03])

ri.WorldEnd()
ri.End()