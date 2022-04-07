#!/usr/bin/env python

import prman

ri = prman.Ri()
filename = "__render"  # "perfume.rib"

##### SETTINGS #####

ri.Begin(filename)
ri.Display("perfume.exr", "it", "rgba")
ri.Format(720, 576, 1)
# ri.Format(1920, 1080, 1)

ri.Hider("raytrace", {"int incremental": [1]})
# ri.ShadingRate(10)
# ri.PixelVariance(0.1)
ri.Integrator("PxrPathTracer", "integrator")
ri.Projection(ri.PERSPECTIVE,{ri.FOV:40})


##### GLOBAL TRANSFORMATION #####

ri.Translate(0, 0, 20)

ri.WorldBegin()

##### LIGHTING #####

ri.TransformBegin()
ri.AttributeBegin()
ri.Declare("domeLight", "string")
ri.Rotate(-90, 1, 0, 0)
# ri.Rotate(deg,0,0,1)
ri.Rotate(-30,0,0,1)
ri.Light("PxrDomeLight", "domeLight", {
    "string lightColorMap": "env/photo_studio_london_hall_8k.tx",
    "float intensity": [0.8]
    })

ri.AttributeEnd()
ri.TransformEnd()

ri.Pattern("shader", "shader",{
    "color cin": [ 0.65, 0.27, 0.07 ]
})

ri.Attribute("displacementbound", {
    "float sphere" : [0.1]
})

ri.Displace("PxrDisplace", "disp", {
    "float dispAmount": [0.1],
    "reference float dispScalar": ["shader:resultF"]
})

# ri.Bxdf("PxrDisney", "bxdf",{
#     "reference color baseColor" : ["shader:Cout"]
# })

# ri.Rotate(-90, 1, 0, 0)
# ri.Geometry("teapot")


ri.Patch("bilinear", {"P": [-5,-5,0, 5,-5,0, -5,5,0, 5,5,0]})


ri.WorldEnd()
ri.End()