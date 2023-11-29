from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 
from numpy import * #libreria matematica 
import sys
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-5.0,5.0,-5.0,5.0)
    #grafica de la parabola 
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(1.0)
        #parabola sin sombra
    for x in arange(-5.0,5.0,0.5):
        y=x**2
        glColor3f(0.0,0.0,0.0)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        #genera la limitante 
        for a in arange(-5.0,5.0,0.01): #ojo,modificar
            if a < x**2:
                glColor3f(0.50,0.50,0.50)
                glBegin(GL_POINTS)
                glVertex2f(x,a)
                glEnd()
        #dibujanddo coordenadas 
        glColor3f(0.0,0.0,0.0)
        glBegin(GL_LINES)
        glVertex2f(-5.0,0.0)
        glVertex2f(5.0,0.0)
        glVertex2f(0.0,5.0)
        glVertex2f(0.0,-5.0)
        glEnd()
        glFlush()

def main ():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(400,400)
    glutCreateWindow("region sombreada")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()

#llmamada al modulo principal 
main()


