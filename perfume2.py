#!/usr/bin/env python
import perfume

ri = perfume.ri

##### SETTINGS #####

ri.Begin("__render")
ri.Display("render/v2.exr", "file", "rgba")
ri.Format(1920, 1080, 1)

ri.Hider("raytrace", {
    "int incremental": [1],
    "int minsamples": 128,
    "int maxsamples": 256
})
ri.ShadingRate(1)
ri.PixelVariance(10)
ri.Integrator("PxrPathTracer", "integrator")

ri.Projection(ri.PERSPECTIVE,{ri.FOV:35})
ri.DepthOfField(8, 0.01, 0.27)

##### GLOBAL TRANSFORMATION #####

# Convert to real life scale
ri.Scale(0.01,0.01,0.01)
ri.Translate(0, 1.2, 28)

ri.WorldBegin()

perfume.lighting()
perfume.env()

ri.TransformBegin()

ri.Translate(10, perfume.bodyRadius-(perfume.bodyHeight+perfume.bottomMinorRadius), -3)
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

ri.WorldEnd()
ri.End()