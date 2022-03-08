import xml.etree.ElementTree as ET
import math

##Dont run this file it does nothing, just provides some global functions for other scripts to utilise

def Vec3ToText(vec3):
        string = str(vec3[0]) + " " + str(vec3[1]) + " " + str(vec3[2])
        return string

def ParseVec3(vec3):
    components = str.split(vec3, " ")
    for i, c in enumerate(components):
        if not c:
            components[i] = 0
        else:
            components[i] = float(c)
    return components

def Color255Normalise(vec3):
    return [vec3[0] / 255, vec3[1] / 255, vec3[2] / 255]

##  Statics for XML tags
BEAMNODE = 'beamnode'
POSITION = 'pos'
BEAM = 'beam'
FREENODE = 'freenode'
CUSTOMCOLOR = 'colormode_custom'
ID = 'id'