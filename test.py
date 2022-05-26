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
# ri.Rotate(-30, 0, 1, 0)

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

# ri.Pattern("shader", "shader",{
#     "color Cin": [ 0.65, 0.27, 0.07 ]
# })

# ri.Attribute("displacementbound", {
#     "float sphere" : [0.1]
# })

# ri.Displace("PxrDisplace", "disp", {
#     "float dispAmount": [1],
#     "reference float dispScalar": ["shader:resultF"]
# })
# ri.Displace("PxrDisplace", "disp", {
#     "float dispAmount": [-0.1],
#     "reference float dispScalar": ["shader:test"]
# })
# ri.Pattern("PxrVoronoise", "noiseTexture",{
#     "float frequency": [5],
#     "float jitter" : [0.5],
#     "float smoothness": [1]
# })

# ri.Pattern("PxrFlakes", "flakes", {
# 	'normal inputNormal' : [0,0,0], 
# 	'float flakeAmount' : [.5], 
# 	'float flakeFreq' : [57.30], 
# 	'float density' : [1.0], 
# 	'float size' : [1.0], 
# 	'int octaves' : [1], 
# 	'float jitter' : [0.75], 
# 	'int validateNormals' : [0], 
# })

# ri.Pattern('PxrMix','mixer',
# {
# 	'color color1' : [0.,0.,0.], 
# 	'color color2' : [1.,1.,1.], 
# 	# 'float mix' : [1], 
# 	'reference float mix' : ["flakes:resultA"], 
# })
# ri.Pattern(
#     "PxrManifold2D",
#     "tileManifold",
#     {
#         # "int numTextures": [1],
#         # "int textureOrder": [0],
#         # "float angle": [45],
#         "float scaleS": [1],
#         "float scaleT": [2],
#         # "int invertT": [0],
#         # "int randomOrientation": [1],
#         # "float randomExtraSeed": [0.12],
#     },
# )


# ri.Pattern("PxrTexture", "myTexture", {
#     "string filename" : ["textures/White_oak_pxr128.tx"],
#     "reference struct manifold": ["tileManifold:result"]
# })

# ri.Pattern("PxrBump", "bump", {
#     "string filename" : ["textures/White_oak_pxr128_bmp.tx"]
# })

# ri.Bxdf("PxrDisney", "bxdf",{
#     "reference color baseColor" : ["myTexture:resultRGB"],
#     # "reference normal bumpNormal":  ["bump:resultN"] 
# })

# ri.Bxdf("PxrDisney", "bxdf",{
#     "color baseColor" : [ 0.65, 0.27, 0.07 ],
#     "float metallic": [0.9],
#     "float anisotropic" : [0.6],
#     "float roughness": [0.3],
#     "reference normal bumpNormal":  ["flakes:resultN"] 
# })
# ri.Bxdf("PxrDisney", "bxdf",{
#     "color baseColor" : [ 0,0,0 ],
#     # "color baseColor" : [ 0.65, 0.27, 0.07 ],
#     "reference normal bumpNormal":  ["flakes:resultN"] 
# })



ri.Pattern("PxrTexture", "wall", {
    "string filename" : ["textures/beige_wall.tx"],
    # "color colorScale" : [1, 1.3, 1],
})

ri.Pattern("PxrNormalMap", "normal", {
    "string filename" : ["textures/beige_wall_normal.tx"],
    # "float bumpScale" : [1]
})

ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["wall:resultRGB"],
    # "color baseColor" : [1,1,1],
    "reference normal bumpNormal":  ["normal:resultN"] 
})

# ri.Rotate(-90, 1, 0, 0)
# ri.Geometry("teapot")


ri.Patch("bilinear", {"P": [-5,-5,0, 5,-5,0, -5,5,0, 5,5,0]})




ri.Bxdf("PxrDisney", "bxdf",{
    "color baseColor" : [1,1,1]
})

ri.Translate(7.5,0,0)

ri.Patch("bilinear", {"P": [-5,-5,0, 5,-5,0, -5,5,0, 5,5,0]})


ri.Pattern("PxrTexture", "table", {
    "string filename" : ["textures/White_oak_pxr128.tx"]
})

ri.Pattern("PxrNormalMap", "normal", {
    "string filename" : ["textures/White_oak_pxr128_normal.tx"]
})

ri.Bxdf("PxrDisney", "bxdf",{
    "reference color baseColor" : ["table:resultRGB"],
    "reference normal bumpNormal":  ["normal:resultN"] 
})


ri.Translate(-15,0,0)

ri.Patch("bilinear", {"P": [-5,-5,0, 5,-5,0, -5,5,0, 5,5,0]})

ri.WorldEnd()
ri.End()