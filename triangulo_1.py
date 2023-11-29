from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

w,h=500,500

def triangle():
    glBegin(GL_TRIANGLES)
    glVertex(100,250)
    glVertex(250,450)
    glVertex(400,250)
    glEnd()

def init():
    glViewport(0,0,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,500,0.0,500,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH)
    glLoadIdentity()
    init()
    triangle()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0,0)      
    glutInitWindowSize(500,400)
    glutCreateWindow("grafica de triangulo")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)  
    glutMainLoop()

main()



    
