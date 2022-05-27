#!/usr/bin/env python

import prman
import math

ri = prman.Ri()

##### SETTINGS #####

ri.Begin("__render")
ri.Display("render/dof.exr", "file", "rgba")
# ri.Display("perfume.exr", "it", "rgba")
# ri.Format(720, 576, 1)
ri.Format(1920, 1080, 1)

ri.Hider("raytrace", {
    "int incremental": [1],
    "int minsamples": 128,
    "int maxsamples": 256
})
ri.ShadingRate(1)
ri.PixelVariance(0.01)
ri.Integrator("PxrPathTracer", "integrator")

# ri.Projection(ri.ORTHOGRAPHIC)
ri.Projection(ri.PERSPECTIVE,{ri.FOV:40})

ri.DepthOfField(2.8, 0.6, 16)

##### GLOBAL TRANSFORMATION #####

# ri.Translate(0, 2.5, 2.5)
ri.Translate(0, 1.2, 17)
ri.Rotate(-30, 1, 0, 0)

ri.WorldBegin()

##### LIGHTING #####

ri.TransformBegin()
ri.AttributeBegin()
ri.Declare("domeLight", "string")
ri.Rotate(-90, 1, 0, 0)
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

ri.Pattern("PxrTexture", "damage", {
    "string filename": "textures/damage.tx"
})

ri.Pattern("shader", "shader",{
    "color Cin": [ 0.6, 0.27, 0.07 ],
    "reference float damage": ["damage:resultR"] 
})

ri.Attribute("displacementbound", {
    "float sphere" : [0.1]
})

ri.Pattern("PxrFlakes", "flakes", {
    'float flakeAmount' : [0.05], 
    'float flakeFreq' : [80], 
    'float size' : [0.8], 
    'int octaves' : [2], 
})

ri.AttributeBegin()

ri.Displace("PxrDisplace", "disp", {
    "float dispAmount": [-0.0001],
    "reference float dispScalar": ["shader:disp2"]
})

ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["shader:Cout2"],
    "float metallic": [0.9],
    "float roughness": [0.3],
    "float anisotropic" : [0.6],
    "reference normal bumpNormal":  ["flakes:resultN"] 
})

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Cylinder(bodyRadius, -bodyHeight, 0, 360)
ri.TransformEnd()
ri.AttributeEnd()

ri.AttributeBegin()

ri.Displace("PxrDisplace", "disp", {
    "float dispAmount": [-0.0001],
    "reference float dispScalar": ["shader:disp"]
})

ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["shader:Cout"],
    "float metallic": [0.9],
    "float roughness": [0.3],
    "float anisotropic" : [0.6],
    "reference normal bumpNormal":  ["flakes:resultN"] 
})

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
    "color baseColor" : [ 0.4, 0.2, 0.02 ],
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

### Desk ###

ri.AttributeBegin()

ri.Pattern("PxrTexture", "desk", {
    "string filename" : ["textures/White_oak_pxr128.tx"]
})

ri.Pattern("PxrNormalMap", "normal", {
    "string filename" : ["textures/White_oak_pxr128_normal.tx"]
})

ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["desk:resultRGB"],
    "reference normal bumpNormal":  ["normal:resultN"] 
})

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Rotate(90,0,0,1)
ri.Translate(0, 0, -(bodyHeight+bottomMinorRadius))
ri.Patch("bilinear", {"P": [-20,-50,0, 10,-50,0, -20,50,0, 10,50,0]})
ri.TransformEnd()

ri.AttributeEnd()

### Wall ###

ri.AttributeBegin()

ri.Pattern("PxrTexture", "wall", {
    "string filename" : ["textures/beige_wall.tx"],
})

ri.Pattern("PxrNormalMap", "normal", {
    "string filename" : ["textures/beige_wall_normal.tx"],
})

ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["wall:resultRGB"],
    "reference normal bumpNormal":  ["normal:resultN"],
    "float roughness": [0.5]
})

ri.TransformBegin()
ri.Translate(0, -(bodyHeight+bottomMinorRadius+1), 15)
ri.Patch("bilinear", {"P": [-50,0,0, 50,0,0, -50,100,0, 50,100,0]})
ri.TransformEnd()

ri.AttributeEnd()


ri.WorldEnd()
ri.End()