from OpenGL.GLUT import*
from OpenGL.GL import*
from OpenGL.GLU import* 
from numpy import* #libreria matematica 
import sys

def init():
    glClear(1.0,1.0,1.0,1.0)
    gluOrtho2D(-5.0,5.0,-5.0,5.0)

def plot_Y():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(3.0)
    for x in arange(-5.0,5.0,0.1):
        y=2*x+7
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        glFlush()
def main():
     glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50,100)
glutCreateWindow("grafica de la linea")
glutDisplayFunc(plot_Y)
init()
glutMainLoop()

#llamar a la funcion principal
main()
#if __name__=="__main__":main()
        
