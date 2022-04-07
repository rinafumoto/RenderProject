#!/usr/bin/env python

import prman
import math

ri = prman.Ri()
filename = "__render"  # "perfume.rib"

# for i in range(12):
    # deg = i*30

##### SETTINGS #####

ri.Begin(filename)
# ri.Display("perfume_"+str(deg)+".exr", "it", "rgba")
ri.Display("perfume.exr", "it", "rgba")
# ri.Format(720, 576, 1)
ri.Format(1920, 1080, 1)

ri.Hider("raytrace", {"int incremental": [1]})
ri.ShadingRate(10)
ri.PixelVariance(0.1)
ri.Integrator("PxrPathTracer", "integrator")

ri.Option( 'statistics', {'filename'  : [ 'stats.txt' ] } )
ri.Option( 'statistics', {'endofframe' : [ 1 ] })

# ri.Projection(ri.ORTHOGRAPHIC)
ri.Projection(ri.PERSPECTIVE,{ri.FOV:40})

##### GLOBAL TRANSFORMATION #####

# ri.Scale(0.1,0.1,0.1)
# ri.Translate(0, 1, 15)
ri.Translate(0, 1.5, 20)
# ri.Translate(0, 100, 0)
ri.Rotate(-30, 1, 0, 0)
# ri.Rotate(-5, 0, 0, 1)
# ri.DepthOfField(5.6, 0.9, 20)

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

##### MODELLING #####

bodyHeight = 6.7
bodyRadius = 1.65
capHeight = 2.8
capRadius = 0.95
middleHeight = 1.3

### Body ###

ri.AttributeBegin()

ri.Pattern("shader", "shader",{
    "color Cin": [ 0.65, 0.27, 0.07 ]
})

ri.Attribute("displacementbound", {
    "float sphere" : [0.001]
})

ri.Displace("PxrDisplace", "disp", {
    "float dispAmount": [0.001],
    "reference float dispScalar": ["shader:resultF"]
})

ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["shader:Cout"],
    "float metallic": [0.9],
    "float anisotropic" : [0.6],
    "float roughness": [0.3]
})

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
ri.Sphere(r, d, r, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Translate(0, 0, -bodyHeight)
bottomMinorRadius = 0.3
degree = -135
ri.Torus(bodyRadius-bottomMinorRadius, bottomMinorRadius, degree, 0, 360)
ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
height = -bodyHeight+math.sin(math.radians(degree))*bottomMinorRadius
radius = bodyRadius-bottomMinorRadius+math.sin(math.radians(degree))*bottomMinorRadius
ri.Disk(height, radius, 360)
ri.TransformEnd()

ri.AttributeEnd()

### Cap ###

ri.AttributeBegin()

ri.TransformBegin()
ri.Translate(0, 0.05, 0)

ri.Bxdf("PxrDisney", "bxdf",{
    "color baseColor" : [ 0.65, 0.27, 0.07 ],
    "float metallic": [1],
    "float roughness": [0]
})

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
ri.TransformEnd()

ri.AttributeEnd()

### Table ###

ri.AttributeBegin()

ri.Pattern("PxrTexture", "myTexture", {
    "string filename" : ["textures/White_oak_pxr128.tx"]
})
ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["myTexture:resultRGB"]
})

# expr = """
# $colour = c1;
# $c = floor( 10 * $u ) +floor( 10 * $v );
# if( fmod( $c, 2.0 ) < 1.0 )
# {
# 	$colour=c2;
# }
# $colour
# """

# ri.Pattern("PxrSeExpr", "seTexture", {"color c1": [1, 1, 1], "color c2": [0, 0, 0], "string expression": [expr]})
# ri.Bxdf(
#     "PxrDiffuse",
#     "diffuse",
#     {
#         #  'color diffuseColor'  : [1,0,0]
#         "reference color diffuseColor": ["seTexture:resultRGB"]
#     },
# )

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Rotate(90,0,0,1)
ri.Translate(-35, 0, -(bodyHeight+bottomMinorRadius))
ri.Patch("bilinear", {"P": [-40,-40,0, 40,-40,0, -40,40,0, 40,40,0]})
ri.TransformEnd()

ri.AttributeEnd()

ri.WorldEnd()
ri.End()