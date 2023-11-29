from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawLetter_P():
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0, 0.5)
    glVertex2f(0, 0.5)
    glVertex2f(0, 0)
    glEnd()

def drawLetter_A():
    glBegin(GL_LINES)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0, -0.5)
    glVertex2f(0, -0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

def drawLetter_U():
    glBegin(GL_LINES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0, 0.5)
    glVertex2f(0, 0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

def drawLetter_L():
    glBegin(GL_LINES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    
    glTranslatef(-1, 0, 0)
    drawLetter_P()
    
    glTranslatef(1, 0, 0)
    drawLetter_A()
    
    glTranslatef(1, 0, 0)
    drawLetter_U()
    
    glTranslatef(1, 0, 0)
    drawLetter_L()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-4, 4, -1, 1)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutCreateWindow("Nombre Paul")
glutDisplayFunc(display)
glutReshapeFunc(reshape)

glutMainLoop()


