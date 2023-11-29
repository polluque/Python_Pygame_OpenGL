import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Dibuja el eje X en rojo
    gl.glColor3f(1.0, 0.0, 0.0)  # Rojo
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(-3.0, 0.0)
    gl.glVertex2f(3.0, 0.0)
    gl.glEnd()

    # Dibuja el eje Y en verde
    gl.glColor3f(0.0, 1.0, 0.0)  # Verde
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(0.0, -1.0)
    gl.glVertex2f(0.0, 1.0)
    gl.glEnd()

    # Dibuja la función y = sin(x) en azul
    gl.glColor3f(0.0, 0.0, 1.0)  # Azul
    gl.glBegin(gl.GL_LINE_STRIP)
    for x in range(-300, 300):
        x /= 100.0  # Escala x para ajustar el rango
        y = math.sin(x)
        gl.glVertex2f(x, y)
    gl.glEnd()

    gl.glFlush()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(600, 400)
    glut.glutCreateWindow("Gráfico de y = sin(x)")

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-3.0, 3.0, -1.0, 1.0, -1.0, 1.0)

    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
