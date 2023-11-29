from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
from numpy import*
import sys

#caracteristicas de la ventana 
def init():
    glClearColor(1.0,1.0,1.0,1.0)  #colorr del fondo de pantalla 
    gluOrtho2D(-5.0,5.0,-5.0,5.0) #dimensiones de mi ventana 

#caracteristicas de la parabola, sera formada por puntos 
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(3.0)

    #ejes de coordenadas 
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,1.0) # color de las coordenadas 
    #x
    glVertex(-5.0,0.0)
    glVertex(5.0,0.0)
    #y
    glVertex(0.0,5.0)
    glVertex(0.0,-5.0)
    glEnd()

    #creando la parabola 
    for x in arange(-5.0,5.0,0.01):
        y=x*x + 2*x +3
        glBegin(GL_POINTS)
        glVertex(x,y)
        glEnd()
        glFlush()
    
#modulo principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)#posicion de origen de coordenadas 
    glutInitWindowSize(400,400)
    glutCreateWindow("grafica de la parabola")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()

#invocando el modulo principal
main()