import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    
    # Define los puntos extremos de la línea
    x1, y1 = -0.5, 0.0
    x2, y2 = 0.5, 1.0
    
    # Calcula la pendiente (m) usando la ecuación punto-pendiente
    m = (y2 - y1) / (x2 - x1)
    
    # Dibuja la línea usando la ecuación punto-pendiente
    gl.glColor3f(1.0, 1.0, 1.0)  # Color blanco
    gl.glBegin(gl.GL_POINTS)
    for x in range(int(x1 * 1000), int(x2 * 1000) + 1):
        x /= 1000.0  # Convierte de int a float
        y = y1 + m * (x - x1)
        gl.glVertex2f(x, y)
    gl.glEnd()
    
    gl.glFlush()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow("Gráfico de Línea con Ecuación Punto-Pendiente")

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
