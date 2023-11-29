"""
#aumento de tamaño de los planetas, aumento del radio 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import * 
import sys

# Valores iniciales
width = 500
height = 500

# Valores iniciales de posición, componentes de velocidad y tiempo incremento
global vx1, vy1, vz1, x1, y1, z1, r2, r3, ax1, ay1, az1, dt
global vx2, vy2, vz2, x2, y2, z2, ax2, ay2, az2, G

# Posiciones iniciales x, y, z para ambas estrellas
x1 = 1.0
y1 = 0.0
z1 = 0.0
x2 = -1.0
y2 = 0.0
z2 = 0.0

# Velocidades iniciales vx, vy, vz para ambas estrellas
vx1 = 0.0
vy1 = -0.128571428
vz1 = 0.0
vx2 = 0.0
vy2 = 0.3
vz2 = 0.0

# Masas iniciales para ambas estrellas
m1 = 0.7
m2 = 0.3
rad1 = 0.5 * m1 #aumentar el tamaño de planeta 1 
rad2 = 0.5 * m2 #aumentar el tamaño de planeta 2

# Constante gravitacional arbitraria "Big G"
G = 1.0

# Calcular la distancia y el denominador r ** 3 para la gravitación universal
r2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
r3 = r2*sqrt(r2)

# Calcular componentes de aceleración a lo largo de los ejes x, y, z
# Primero para m1
ax1 = -G * (x1 - x2) * m2 / r3
ay1 = -G * (y1 - y2) * m2 / r3
az1 = -G * (z1 - z2) * m2 / r3

# Ahora por m2
ax2 = -G * (x2 - x1) * m1 / r3
ay2 = -G * (y2 - y1) * m1 / r3
az2 = -G * (z2 - z1) * m1 / r3

# Este valor mantiene una órbita suave
dt = 0.001


# Lista para almacenar las posiciones anteriores de las estrellas
prev_positions1 = []
prev_positions2 = []


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)


def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1.0, 1.0, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def keyboard(key, x, y):
    if key == chr(27):
        sys.exit()
    if key == "q":
        sys.exit()


def orbits():
    global vx1, vy1, vz1, x1, y1, z1, r2, r3, ax1, ay1, az1
    global vx2, vy2, vz2, x2, y2, z2, ax2, ay2, az2
    global prev_positions1, prev_positions2

    vx1 += 0.5 * ax1 * dt
    vy1 += 0.5 * ay1 * dt
    vz1 += 0.5 * az1 * dt
    vx2 += 0.5 * ax2 * dt
    vy2 += 0.5 * ay2 * dt
    vz2 += 0.5 * az2 * dt

    x1 += vx1 * dt
    y1 += vy1 * dt
    z1 += vz1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt
    z2 += vz2 * dt

    r2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
    r3 = r2 * sqrt(r2)

    ax1 = -G * (x1 - x2) * m2 / r3
    ay1 = -G * (y1 - y2) * m2 / r3
    az1 = -G * (z1 - z2) * m2 / r3

    ax2 = -G * (x2 - x1) * m1 / r3
    ay2 = -G * (y2 - y1) * m1 / r3
    az2 = -G * (z2 - z1) * m1 / r3

    vx1 += 0.1 * ax1 * dt
    vy1 += 0.1 * ay1 * dt
    vz1 += 0.1 * az1 * dt
    vx2 += 0.1 * ax2 * dt
    vy2 += 0.1 * ay2 * dt
    vz2 += 0.1 * az2 * dt

    # Almacenar las posiciones anteriores en las listas
    prev_positions1.append((x1, y1, z1))
    prev_positions2.append((x2, y2, z2))

    # Mantener solo las últimas 100 posiciones
    if len(prev_positions1) > 100:
        prev_positions1 = prev_positions1[-100:]
    if len(prev_positions2) > 100:
        prev_positions2 = prev_positions2[-100:]

    glutPostRedisplay()


def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)

    # Dibujar órbitas
    glColor3ub(100, 100, 100)
    glLineWidth(1.0)

    glBegin(GL_LINE_STRIP)
    for pos in prev_positions1:
        glVertex3f(pos[0], pos[1], pos[2])
    glEnd()

    glBegin(GL_LINE_STRIP)
    for pos in prev_positions2:
        glVertex3f(pos[0], pos[1], pos[2])
    glEnd()

    # Dibujar estrellas
    # Dibujar estrellas
    glPushMatrix()
    glTranslatef(x1, y1, z1)
    glColor3ub(245, 230, 100)
    glutSolidSphere(rad1, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(x2, y2, z2)
    glColor3ub(245, 150, 30)
    glutSolidSphere(rad2, 10, 10)
    glPopMatrix()

    # Intercambiar los búferes de dibujo
    glutSwapBuffers()


def main():
    global width
    global height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow("Gravitacion Universal")
    glutReshapeFunc(reshape)
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(orbits)
    init()
    glutMainLoop()


main()
"""


"""
#dibujo de las orbitas 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Valores iniciales
width = 500
height = 500

# Valores iniciales de posición, componentes de velocidad y tiempo incremento
global vx1, vy1, vz1, x1, y1, z1, r2, r3, ax1, ay1, az1, dt
global vx2, vy2, vz2, x2, y2, z2, ax2, ay2, az2, G

# Posiciones iniciales x, y, z para ambas estrellas
x1 = 1.0
y1 = 0.0
z1 = 0.0
x2 = -1.0
y2 = 0.0
z2 = 0.0

# Velocidades iniciales vx, vy, vz para ambas estrellas
vx1 = 0.0
vy1 = -0.128571428
vz1 = 0.0
vx2 = 0.0
vy2 = 0.3
vz2 = 0.0

# Masas iniciales para ambas estrellas
m1 = 0.7
m2 = 0.3
rad1 = 0.1 * m1
rad2 = 0.1 * m2

# Constante gravitacional arbitraria "Big G"
G = 1.0

# Calcular la distancia y el denominador r ** 3 para la gravitación universal
r2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
r3 = r2 * math.sqrt(r2)

# Calcular componentes de aceleración a lo largo de los ejes x, y, z
# Primero para m1
ax1 = -G * (x1 - x2) * m2 / r3
ay1 = -G * (y1 - y2) * m2 / r3
az1 = -G * (z1 - z2) * m2 / r3

# Inicializar OpenGL
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutCreateWindow("Simulación de Gravitación Universal")

# Función para dibujar las órbitas
def draw_orbits():
    glColor3f(1.0, 1.0, 1.0)  # Establecer el color de la línea (blanco en este caso)
    glBegin(GL_LINE_LOOP)  # Iniciar el dibujo de una línea continua

    num_points = 100  # Número de puntos para dibujar la órbita
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = math.cos(angle)
        y = math.sin(angle)
        glVertex3f(x, y, 0.0)  # Agregar un punto a la órbita

    glEnd()  # Finalizar el dibujo de la línea continua

# Función para dibujar las estrellas
def draw_stars():
    # Dibujar la primera estrella
    glPushMatrix()
    glTranslatef(x1, y1, z1)
    glColor3f(1.0, 0.0, 0.0)  # Establecer el color de la estrella (rojo en este caso)
    glutSolidSphere(rad1, 20, 20)  # Dibujar una esfera sólida para representar la estrella
    glPopMatrix()

    # Dibujar la segunda estrella
    glPushMatrix()
    glTranslatef(x2, y2, z2)
    glColor3f(0.0, 0.0, 1.0)  # Establecer el color de la estrella (azul en este caso)
    glutSolidSphere(rad2, 20, 20)  # Dibujar una esfera sólida para representar la estrella
    glPopMatrix()

# Función para actualizar las posiciones de las estrellas
def update_positions(dt):
    global x1, y1, z1, x2, y2, z2

    # Actualizar las posiciones utilizando las velocidades actuales y el tiempo incremento dt
    x1 += vx1 * dt
    y1 += vy1 * dt
    z1 += vz1 * dt

    x2 += vx2 * dt
    y2 += vy2 * dt
    z2 += vz2 * dt

# Función para actualizar las velocidades de las estrellas
def update_velocities(dt):
    global vx1, vy1, vz1, vx2, vy2, vz2

    # Calcular la distancia y el denominador r ** 3 para la gravitación universal
    r2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
    r3 = r2 * math.sqrt(r2)

    # Calcular componentes de aceleración a lo largo de los ejes x, y, z para ambas estrellas
    ax1 = -G * (x1 - x2) * m2 / r3
    ay1 = -G * (y1 - y2) * m2 / r3
    az1 = -G * (z1 - z2) * m2 / r3

    ax2 = G * (x1 - x2) * m1 / r3
    ay2 = G * (y1 - y2) * m1 / r3
    az2 = G * (z1 - z2) * m1 / r3

    # Actualizar las velocidades utilizando las aceleraciones actuales y el tiempo incremento dt
    vx1 += ax1 * dt
    vy1 += ay1 * dt
    vz1 += az1 * dt

    vx2 += ax2 * dt
    vy2 += ay2 * dt
    vz2 += az2 * dt

# Función para animar la simulación
def animate():
    dt = 0.01  # Incremento de tiempo para cada iteración de animación

    update_positions(dt)
    update_velocities(dt)

    glutPostRedisplay()  # Marcar la ventana como necesitando ser redibujada

# Función para manejar el evento de dibujo de la ventana de OpenGL
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_stars()  # Dibujar las estrellas en la posición actual

    draw_orbits()  # Dibujar las órbitas de las estrellas

    glutSwapBuffers()

# Configurar OpenGL y ejecutar el bucle principal de OpenGL
glutDisplayFunc(display)
glutIdleFunc(animate)
glutMainLoop()

"""