import math
from turtle import color
import xml.etree.ElementTree as ET
import SupportGen as SG

#---------------------------STATICS--------------------------------
MAXRES = 64

_index = -1
#----------------------------FUNCS---------------------------------

def GetFreeID():
    global _index
    _index += 1
    return _index

def lerp(a : float, b : float, f : float) -> float:
    return a + f * (b - a)


#---------------------------CREATORS-------------------------------

def CreateConstLine(d, p1, p2, c):
    n = ET.SubElement(d, SG.FREENODE, id=str(GetFreeID()))
    ET.SubElement(n, SG.POSITION).text = SG.Vec3ToText(p1)
    n = ET.SubElement(d, SG.FREENODE, id=str(GetFreeID()))
    ET.SubElement(n, SG.POSITION).text = SG.Vec3ToText(p2)

def CreateBeamNodeAtPos(beam, pos):
    return ET.SubElement(beam, SG.BEAMNODE, id=(str(GetFreeID())), pos=str(pos), type='0')

def CreateBeam(n1, n2, t, s1, s2):
    return ET.SubElement(doc, SG.BEAM, start=str(n1), end=str(n2), type=str(t), size1=str(s1),size2=str(s2))

def CreateLineGradientBetween(p1, p2):
    #   Create free nodes
    n1 = ET.SubElement(doc, SG.FREENODE, id=str(GetFreeID()))
    ET.SubElement(n1, SG.POSITION).text = SG.Vec3ToText(p1)
    n2 = ET.SubElement(doc, SG.FREENODE, id=str(GetFreeID()))
    ET.SubElement(n2, SG.POSITION).text = SG.Vec3ToText(p2)

    # Store free node ids
    n1id, n2id = n1.attrib[SG.ID], n2.attrib[SG.ID]

    b1 = CreateBeam(n1id, n2id, 0, 0, 0)
    b2 = CreateBeam(n1id, n2id, 0, 0, 0)

    b1bNodes = {}
    b2bNodes = {}

    tColor = {}

    bNodeCount = _colorres
    for i in range(bNodeCount + 1):
        percent = i / bNodeCount

        b1bNodes[i] = CreateBeamNodeAtPos(b1, percent)
        b2bNodes[i] = CreateBeamNodeAtPos(b2, percent)

        if i >= 1:
            beam = CreateBeam(b1bNodes[i-1].attrib[SG.ID], b2bNodes[i].attrib[SG.ID], 0, _supportDiameter, _supportDiameter)
            tColor = [lerp(_color1[0], _color2[0], percent), lerp(_color1[1], _color2[1], percent), lerp(_color1[2], _color2[2], percent)]
            ET.SubElement(beam, SG.CUSTOMCOLOR, r=str(tColor[0]), g=str(tColor[1]), b=str(tColor[2]))

#----------------------------LOGIC---------------------------------

_arg0 = "Gradient line"
_arg1 = "Gradient circle [Not supported]"
_arg2 = "Gradient spiral [Not supported]"

_func = input("Enter type [0: " + _arg0 + ", 1: " + _arg1 + ", 2: " + _arg2 + "] : ") or '0'

_color1 = input("Enter colour 0-255 [r g b] : ") or '0 0 0'
_color2 = input("Enter colour 0-255 [r g b] : ") or '255 255 255'
_colorres = input("Enter resolution of colour [Amount of steps 1 - " + str(MAXRES) +"] : ") or 4
_colorres = max(min(int(_colorres), MAXRES), 1)

_color1 = SG.ParseVec3(_color1)
_color2 = SG.ParseVec3(_color2)

_color1 = SG.Color255Normalise(_color1)
_color2 = SG.Color255Normalise(_color2)

_supportDiameter = input("Enter a support size : ") or 0.5

# Create xml table
root = ET.Element("root")
doc = ET.SubElement(root, "supports")

_func = int(_func)

if _func == 0:
        #--Create gradient line
        print("Creating colour gradient line file...")
        _pos1 = input("Enter first node position [x y z] : ") or '0 2 0'
        _pos2 = input("Enter second node position [x y z] : ") or '0 7 0'
        _pos1 = SG.ParseVec3(_pos1)
        _pos2 = SG.ParseVec3(_pos2)

        CreateLineGradientBetween(_pos1, _pos2)
elif _func == 1:
        #--Create gradient circle
        input("Not supported currently! [press any key to close]")
elif _func == 2:
        #--Create gradient spiral
        input("Not supported currently! [press any key to close]")
else:
    input("I- use the numbers provided! its not that hard!")


tree = ET.ElementTree(root)
tree.write("Gradient.xml")

input("Created file! [Press any key to close]")