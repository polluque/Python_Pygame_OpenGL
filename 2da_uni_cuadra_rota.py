import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),  # Vértice superior
    (1, -1, 0),  # Vértice inferior derecho
    (-1, -1, 0)  # Vértice inferior izquierdo
)

colores = (
    (1, 0, 0),  # Rojo
    (0, 1, 0),  # Verde
    (0, 0, 1)  # Azul
)

# Definir aristas y caras
bordes = (
    (0, 1),  # borde superior
    (1, 2),  # borde derecho
    (2, 0)  # borde izquierdo
)

caras = (
    (0, 1, 2),  # Triángulo compuesto por los vértices 0, 1 y 2
)

def triangle():
    glBegin(GL_TRIANGLES)
    for cara in caras:
        for vertex in cara:
            glColor3fv(colores[vertex])  # Asignar color al vértice
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
        triangle()
        pygame.display.flip()
        pygame.time.wait(10)

main()


"""import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),  # Vértice superior
    (1, -1, 0),  # Vértice inferior derecho
    (-1, -1, 0),  # Vértice inferior izquierdo
)

# bordes
bordes = (
    (0, 1),  # BORDE superior
    (1, 2),  # BORDE derecho
    (2, 0),  # BORDE izquierdo
)

def triangle():
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
        triangle()
        pygame.display.flip()
        pygame.time.wait(10)

main()
"""


"""import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),  # Vértice superior
    (1, -1, 0),  # Vértice inferior derecho
    (-1, -1, 0)  # Vértice inferior izquierdo
)

bordes = (
    (0, 1),
    (1, 2),
    (2, 0)
)

def triangle():
    glBegin(GL_LINES)
    for edge in bordes:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_ejes():
    glBegin(GL_LINES)
    # Eje X (rojo)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)
    # Eje Y (verde)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2, 0)
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
        draw_ejes()  # Dibuja los ejes X y Y
        triangle()
        pygame.display.flip()
        pygame.time.wait(10)

main()"""





"""import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1,-1,0),
    (1,1,0),
    (-1,1,0),
    (-1,-1,0),
    (1,-1,0),
    (1,1,0),
    (-1,-1,0),
    (-1,1,0)
    )
#aristas

bordes =(
    (6,4),
    (6,7),
    (5,4),
    (5,7)
    )

def square():
    glBegin(GL_LINES)
    for edge in bordes:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45,(display[0]/display[1]),0.1,50.0)

    glTranslatef(0.0,0.0,-5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        square()
        pygame.display.flip() #animacion automatica
        pygame.time.wait(10)
main()"""

