#!/usr/bin/env python
import perfume

ri = perfume.ri

bodyHeight = 6.7
bodyRadius = 1.65
capHeight = 2.8
capRadius = 0.95
middleHeight = 1.3
bottomMinorRadius = 0.3

##### SETTINGS #####

ri.Begin("__render")
ri.Display("perfume.exr", "it", "rgba")
# ri.Display("render/perfume_v2.exr", "file", "rgba")
ri.Format(1920, 1080, 1)
# ri.Format(720, 576, 1)

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
# ri.DepthOfField(2.8, 0.6, 16)

##### GLOBAL TRANSFORMATION #####

ri.Translate(0, 1.2, 28)
# ri.Translate(0, 1.2, 24)
# ri.Translate(0, 1.2, 17)
# ri.Translate(0, 0, 17)
# ri.Translate(0, (bodyHeight+bottomMinorRadius), 0)


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
perfume.bottle()

ri.Translate(5,0,0)
ri.TransformBegin()
ri.Rotate(90, 0,1,0)
perfume.bottle()
ri.TransformEnd()

ri.Translate(5,0,0)
ri.TransformBegin()
ri.Rotate(90, 0,1,0)
perfume.bottle()
ri.TransformEnd()

ri.Translate(5,0,0)
ri.TransformBegin()
ri.Rotate(90, 0,1,0)
perfume.bottle()
ri.TransformEnd()

ri.TransformEnd()

ri.WorldEnd()
ri.End()