#simualacion de un sistema planetario 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (800, 600)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)

# Crear esferas para representar planetas
planet1 = gluNewQuadric()
planet2 = gluNewQuadric()
planet3 = gluNewQuadric()

# Color del sol (círculo en el centro)
sun_color = [1.0, 1.0, 0.0, 1.0]  # RGBA

# Posiciones y tamaños iniciales de los planetas
planet_positions = [(0, 0, 0), (3, 0, 0), (6, 0, 0)]
planet_sizes = [1.0, 0.7, 0.5]
planet_speeds = [1.0, 0.5, 0.2]

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)

viewMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
glLoadIdentity()

displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
up_down_angle = 0.5
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False

    keypress = pygame.key.get_pressed()
    glLoadIdentity()
    glPushMatrix()
    glLoadIdentity()

    keypress = pygame.key.get_pressed()
    up_down_angle = mouseMove[0] * 0.5
    glRotatef(up_down_angle, 0.0, 0.0, 5)

    if keypress[pygame.K_UP]:
        glTranslatef(0, 0, 0.1)
    if keypress[pygame.K_DOWN]:
        glTranslatef(0, 0, -0.1)
    if keypress[pygame.K_LEFT]:
        glTranslatef(-0.1, 0, 0)
    if keypress[pygame.K_RIGHT]:
        glTranslatef(0.1, 0, 0)

    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glPopMatrix()
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)

    # Definir propiedades de material para el sol
    glMaterialfv(GL_FRONT, GL_AMBIENT, sun_color[:3])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, sun_color[:3])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, 50.0)

    # Definir posición de luz
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])

    # Dibujar el sol
    glPushMatrix()
    glTranslatef(0, 0, 0)
    gluSphere(planet1, 0.3, 32, 16)  # Ajusta el tamaño del sol según sea necesario
    glPopMatrix()

    # Dibujar planetas
    for i, (x, y, z) in enumerate(planet_positions):
        glPushMatrix()
        glTranslatef(x, y, z)
        glColor4f(1.0, 0.5, 0.0, 0.0)
        gluSphere([planet1, planet2, planet3][i], planet_sizes[i], 32, 16)
        glPopMatrix()

        # Rotar planetas alrededor de su propio eje
        glRotatef(planet_speeds[i], 0, 1, 0)
        planet_positions[i] = (
            x * math.cos(math.radians(planet_speeds[i])) - z * math.sin(math.radians(planet_speeds[i])),
            y,
            x * math.sin(math.radians(planet_speeds[i])) + z * math.cos(math.radians(planet_speeds[i]))
        )

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()



"""
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)

# Crear esfera
sphere = gluNewQuadric()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)

viewMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
glLoadIdentity()

displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
pygame.mouse.set_pos(displayCenter)
mouseMove = [0, 0]
up_down_angle = 0.5
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False

    keypress = pygame.key.get_pressed()
    glLoadIdentity()
    glPushMatrix()
    glLoadIdentity()

    keypress = pygame.key.get_pressed()
    up_down_angle = mouseMove[0] * 0.5
    glRotatef(up_down_angle, 0.0, 0.0, 5)

    if keypress[pygame.K_UP]:
        glTranslatef(0, 0, 0.1)
    if keypress[pygame.K_DOWN]:
        glTranslatef(0, 0, -0.1)
    if keypress[pygame.K_LEFT]:
        glTranslatef(-0.1, 0, 0)
    if keypress[pygame.K_RIGHT]:
        glTranslatef(0.1, 0, 0)

    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glPopMatrix()
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)

    # Definir propiedades de material
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.5, 0.5, 0.5, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, 50.0)

    # Definir posición de luz
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])

    glPushMatrix()
    glTranslatef(-1.5, 0, 0)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    gluSphere(sphere, 1.0, 32, 16)
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
"""



"""
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math 

pygame.init()
display = (800,600)
screen=pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)


#crear esfera
sphere =gluNewQuadric()
#matriz
glMatrixMode(GL_PROJECTION)
#perspective
gluPerspective(45,(display[0]/display[1]),0.1,50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0,-8,0,0,0,0,0,0,1)

viewMatrix=glGetFloat(GL_MODELVIEW_MATRIX)
glLoadIdentity()
#comandos de teclado 
displayCenter=[screen.get_size()[i]//2 for i in range(2)]
mouseMove=[0,0]
pygame.mouse.set_pos(displayCenter)
up_down_agle=0.5
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE or event.key==pygame.K_RETURN:
                run=False
    keypress=pygame.key.get_pressed()
    #visualizar el view matrix 
    glLoadIdentity()
    #inicializar el view matrix
    glPushMatrix()
    glLoadIdentity()

    keypress=pygame.key.get_pressed()
    up_down_agle=mouseMove[0]*0.5
    glRotatef(up_down_agle,0.0,0.0,5)
#aplicar los movimientos de tecla 
    if keypress[pygame.K_UP]:
        glTranslatef(0,0,0.1)
    if keypress[pygame.K_DOWN]:
        glTranslatef(0,0,-0.1)
    if keypress[pygame.K_LEFT]:
        glTranslatef(-0.1,0,0)
    if keypress[pygame.K_RIGHT]:
        glTranslatef(0.1,0,0)


    glMultMatrixf(viewMatrix) 
    viewMatrix=glGetFloatv(GL_MODELVIEW_MATRIX) 
    #Aplicar la matriz g
    glPopMatrix() 
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix() 
    glTranslatef(-1.5,0,0) 
    glColor4f(1.0, 0.5, 0.0, 0.0)

    glEnable(GL_LIGHTING) 
    glEnable(GL_LIGHT0)
    
    gluSphere(sphere, 1.0, 32, 16) 
    #gluSphere(sphere,0.5,30,14) 
    glPopMatrix()
    
    #Movimiento
    pygame. display. flip() 
    pygame.time.wait(10)

pygame. quit()   
"""