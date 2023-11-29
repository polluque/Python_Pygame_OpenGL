import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_P():
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, 0.1)
    glVertex2f(0.5, 0.1)
    glVertex2f(-0.5, 0.1)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.5, -0.1)
    glVertex2f(0.5, -0.1)
    glVertex2f(0.5, -0.1)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(-0.5, -0.5)
    glEnd()

def transform():
    glTranslatef(0 , 0, 0.5) # Traslación en el eje x
    glRotatef(45, 1, 1, 0) # Rotación de 45 grados en el eje 

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1) # Color blanco
    glLoadIdentity()
    transform() # Aplicar transformación
    draw_P() # Dibujar letra "P"
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutCreateWindow("traslacion y rotacion de la letra P ")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()

