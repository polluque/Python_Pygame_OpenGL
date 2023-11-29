import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glClearColor(1.0,1.0,1.0,1.0)

    # Dibuja el eje X
    gl.glColor3f(0.0, 0.0, 0.0)  # negro
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(-1.0, 0.0)
    gl.glVertex2f(1.0, 0.0)
    gl.glEnd()

    # Dibuja el eje Y 
    gl.glColor3f(0.0, 0.0, 0.0)  # negro
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(0.0, -1.0)
    gl.glVertex2f(0.0, 1.0)
    gl.glEnd()

   # dibujo del punto 
    gl.glColor3f(0.0,0.0,1.0) # color del punto 
    gl.glPointSize(10.0)
    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2f(1.0,1.0)#encargado de dibujar la funcion, coordenadas
    gl.glEnd()


    gl.glFlush()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow("Eje de Coordenadas")

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-1.5, 1.5, -1.5, 1.5, -1.0, 1.0)
    glut.glutDisplayFunc(display)
    #glut.glutDisplayFunc(plot_point)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
