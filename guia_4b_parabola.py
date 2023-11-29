from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 
from numpy import * #libreria matematica 
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(3.0)

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0) #color de la linea y puntos
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()

    for x in arange(-5.0, 5.0, 0.1):
        y = x*x
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        glFlush()

    def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowPosition(50,50)
        glutInitWindowSize(400,400)
        glutCreateWindow("function plotter")
        glutDisplayFunc(plotfunc)
        init()
        glutMainLoop()
    main()   
       
    
    