'''
Created on 26 mars 2012

@author: num3ric
'''
import math
from pandac.PandaModules import LineSegs, NodePath
from pandac.PandaModules import deg2Rad, rad2Deg 
from panda3d.core import Vec4


def makeArc(color, angle_degrees = 360, numsteps = 16, horizon_plane = 0,): 
    ls = LineSegs() 
    ls.setColor(color)
    angleRadians = deg2Rad(angle_degrees) 

    for i in xrange(numsteps + 1): 
        a = angleRadians * i / numsteps 
        y = math.sin(a) 
        x = math.cos(a) 

        ls.drawTo(x, y, horizon_plane)
        ls.setThickness(2.0)
        ls.setColor(color)
    node = ls.create() 
    return NodePath(node)