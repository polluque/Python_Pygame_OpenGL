#dibujo de una linea 
from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) #color de fondo de pantalla 
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,200.0,0.0,150.0)

def linea():
    glClear(GL_COLOR_BUFFER_BIT)    
    glColor3f(0.0,0.0,0.0) #color de la linea 
    glBegin(GL_LINES)
    glVertex(20,15) #coordenadas_punto_A
    glVertex(60,50)#coordenadas_punto_b
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,100)
    glutCreateWindow("grafica de la linea")
    init()
    glutDisplayFunc(linea)
    glutMainLoop()

if __name__=="__main__":main()
