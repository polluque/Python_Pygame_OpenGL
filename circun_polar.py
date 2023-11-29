from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def drawacircle():
    glColor3f(0.0,1.0,0.0)
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for i in range (180,360):