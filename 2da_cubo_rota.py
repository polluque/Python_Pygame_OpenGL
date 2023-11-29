"""
#piramide alambrada
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)  # Vértice superior (vértice de la pirámide)
)

bordes = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4)
)

def piramide():
    glBegin(GL_LINES)
    for edge in bordes:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        piramide()
        pygame.display.flip()
        pygame.time.wait(10)

main()
"""
"""
#cubo_alambrado 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)

)


bordes = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
)

caras = (
    (1, 0, 3, 2),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (0, 4, 7, 3),
    (1, 5, 6, 2)
)

#colores de degradado 
def colores_degradado():
    glBegin(GL_QUADS)
    for cara in caras:
        for i, vertice in enumerate(cara):
            color = i / len(cara)  # De 0 a 1 para interpolación lineal
            glColor3f(color, 0.5, 1.0 - color)  # RGB color
            glVertex3fv(vertices[vertice])
    glEnd()


def cubo ():
    glBegin(GL_LINES)
    for edge in bordes:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


#ejes de coordenadas 
def ejes():
    # Eje X (rojo)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(4, 0, 0)
    glEnd()

    # Eje Y (verde)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 4, 0)
    glEnd()

    # Eje Z (azul)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 4)
    glEnd()



def main ():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #glRotatef(1, 3, 1, 1)
            if event. type == pygame.KEYDOWN: 
                if event.key == pygame. K_LEFT: 
                    glTranslatef(-0.5,0,0) 
                if event.key == pygame. K_RIGHT : 
                    glTranslatef(0.5,0,0)
                if event.key == pygame. K_UP: 
                    glTranslatef(0,1,0) 
                if event.key == pygame. K_DOWN: 
                    glTranslatef(0, -1,0)
            
            if event. type == pygame. MOUSEBUTTONDOWN: 
                if event. button == 4: 
                    glTranslatef(0,0,1.0)
                
                if event.button == 5: 
                    glTranslatef(0,0,-1.0)
        
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        ejes()
        colores_degradado()
        cubo()
        pygame.display.flip()
        pygame.time.wait(13)

main()
"""

#piramide, alambrada usando el codigo anterior
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)  # Vértice superior de la pirámide
)

caras = (
    (0, 1, 2, 3),
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4)
)

# Colores de degradado
def colores_degradado():
    glBegin(GL_QUADS)
    for cara in caras:
        for i, vertice in enumerate(cara):
            color = i / len(cara)  # De 0 a 1 para interpolación lineal
            glColor3f(color, 0.5, 1.0 - color)  # RGB color
            glVertex3fv(vertices[vertice])
    glEnd()

# Bordes de la pirámide
def piramide():
    glBegin(GL_LINES)
    for cara in caras:
        for vertice in cara:
            glVertex3fv(vertices[vertice])
    glEnd()

# Ejecución principal
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        colores_degradado()
        piramide()
        pygame.display.flip()
        pygame.time.wait(13)

main()





"""
cubo con rota,trasla,esca
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)  # Vértice superior (vértice de la pirámide)
)

caras = (
    (0, 1, 2),  # Cara frontal
    (0, 2, 3),  # Cara trasera
    (0, 1, 4),  # Cara derecha
    (1, 2, 4),  # Cara izquierda
    (2, 3, 4),  # Cara inferior
    (3, 0, 4)   # Cara superior
)

def piramide():
    glBegin(GL_TRIANGLES)
    for cara in caras:
        for vertice in cara:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Rotación
        glTranslatef(0.01, 0, 0)  # Traslación
        glScalef(1.001, 1.001, 1.001)  # Escalación

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        piramide()
        pygame.display.flip()
        pygame.time.wait(10)

main()
"""






"""import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
)

# Definir caras
caras = (
    (0, 1, 2, 3),  # Cara trasera
    (4, 5, 6, 7),  # Cara frontal
    (0, 1, 5, 4),  # Cara derecha
    (2, 3, 7, 6),  # Cara izquierda
    (0, 3, 7, 4),  # Cara inferior
    (1, 2, 6, 5)   # Cara superior
)

colores = (
    (1, 0, 0),  # Rojo
    (0, 1, 0),  # Verde
    (0, 0, 1),  # Azul
    (1, 1, 0),  # Amarillo
    (1, 0, 1),  # Magenta
    (0, 1, 1)   # Cian
)

def cubo():
    glBegin(GL_QUADS)
    for i, cara in enumerate(caras):
        for j, vertice in enumerate(cara):
            glColor3fv(colores[i])  # Aplica color de la cara
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cubo()
        pygame.display.flip()
        pygame.time.wait(13)

main()
"""

'''
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)  # Vértice superior (vértice de la pirámide)
)

# Definir caras
caras = (
    (0, 1, 2),  # Cara frontal
    (0, 2, 3),  # Cara trasera
    (0, 1, 4),  # Cara derecha
    (1, 2, 4),  # Cara izquierda
    (2, 3, 4),  # Cara inferior
    (3, 0, 4)   # Cara superior
)

def piramide():
    glBegin(GL_TRIANGLES)
    for cara in caras:
        for vertice in cara:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, OPENGL | DOUBLEBUF, 32)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(0.0, 0.0, 0.0, 0.0)  # Fondo transparente
        glClear(GL_COLOR_BUFFER_BIT)
        piramide()
        pygame.display.flip()
        pygame.time.wait(10)

main()
'''