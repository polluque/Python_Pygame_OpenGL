from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from numpy import*
import numpy as np
import math  #libreria para plotear funciones trigonometricas y logaritmicas 
import sys

#
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-5.0,5.0,-5.0,5.0)

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0) #color negro
    glPointSize(1.0)#eje de coordenadas 
    glBegin(GL_LINES)      
    glVertex2f(-4.0,0.0) #grafica de un punto en las abcisas, horizontal
    glVertex2f(4.0,0.0)#grafica de un punto en las ordenadas, horizontal
    glVertex2f(0.0,2.0) #vertical, ordenadas  
    glVertex2f(0.0,-2.0)#vertical, ordenadas#todo el codigo anterior solo es para el dibujo del eje coordenadas  
    glEnd

    #plotear parametros 
    glPointSize(3)
    glBegin(GL_POINTS)
    for px in np.arange(0, 15, 0.025):    
        glColor3f(0, 0, 255 ) #azul
        glVertex2f(px,math.sin(px))
        glColor3f(0, 255, 0) #verde
        glVertex2f(px,math.cos(px)) 
        glEnd()
        glFlush()
#modulo principal
    def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(500,400)
        glutInitWindowPosition(50,50)      
        glutCreateWindow("grafica de la funcion seno y coseno")
        glutDisplayFunc(plotfunc)  
        init()
        glutMainLoop()
    main()



