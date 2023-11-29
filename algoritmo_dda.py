import sys
import time
from OpenGL import* 
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
# dando tamaño a la ventana 
window=0 #variable global 
width, height=800,600 #ancho y alto de la ventana, variables locales 

def lineDDA(x1,y1,x2,y2): #coordenadas
    m=(y2-y1)/(x2-x1)
    x=x1
    y=y1
    #for
    while(x<x2+1):
        glVertex2f(x,y)
        x=x+1
        y=y+m

#funcion que otorga caracteristicas
def line():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)#limpieza de la interfaz 
    glBegin(GL_LINES)
    glColor(0.0,1.0,0.0)
    lineDDA(50,50,350,350)
    glEnd
    glutSwapBuffers()
#encargado de dar todo los privilegios para poder trabajar 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(0,0)
    glutCreateWindow("algoritmo DDA")
    glClearColor(1.0,1.0,1.0,1.0) #color de fondo de la ventana 
    gluOrtho2D(0.0,500.0,0.0,400.0)
    glutDisplayFunc(line)
    glutIdleFunc(line)
    glutMainLoop()
#llamar al modulo principal
main()

    