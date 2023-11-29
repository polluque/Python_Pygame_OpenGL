import pygame as pg
from pygame.locals import*
import OpenGL
from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*

#limpiar ventana
def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

#dibujar punto
def plot_point():
    glClear(GL_COLOR_BUFFER_BIT) # limpia la ventana de dibujos anteriores 
    glColor3f(1.0,0.0,0.0) #color del punto 
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(-0.5,-0.5) #encargado de dibujar la funcion, coordenadas
    #2do_punto
    glColor3f(0.0,1.0,0.0) #color del punto 
    glVertex2f(0.5,0.5)
    #3er_punto
    glColor3f(0.0,0.0,1.0) #color del punto 
    glVertex2f(-0.5,0.5)
    #4to_punto
    glColor3f(1.0,1.0,0.0) #color del punto 
    glVertex2f(0.5,-0.5)
    glEnd()
    glFlush()



#modulo principal 
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(700,500)
glutInitWindowPosition(100,-100)
glutCreateWindow("Dibujando punto")
glutDisplayFunc(plot_point)
glutIdleFunc(clearScreen)
glutMainLoop()