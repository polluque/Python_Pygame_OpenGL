from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Dibuja el eje X en rojo
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glBegin(GL_LINES)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)
    glEnd()

    # Dibuja el eje Y en verde
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glBegin(GL_LINES)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()

    # Dibuja la función y = sin(3x) en azul
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glBegin(GL_LINE_STRIP)
    for x in range(-300, 300):
        x /= 100.0  # Escala x para ajustar el rango
        y = math.sin(3 * x)  # Función y = sin(3x)
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 400)
    glutCreateWindow("Gráfico de y = sin(3x)")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -1.0, 1.0, -1.0, 1.0)

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
