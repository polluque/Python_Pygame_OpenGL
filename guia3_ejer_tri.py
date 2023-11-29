from OpenGL.GLUT import*
from OpenGL.GL import*
from OpenGL.GLU import*             

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,200.0,0.0,150.0)

def linea():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex(20,15) #coord_punto_a
    glVertex(60,50) #coord_punto_b
    glEnd()
    glFlush()

    #main 
    def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowPosition(50,100)
        glutCreateWindow("grafica de la linea")
        init()
        glutDisplayFunc(linea)
        glutMainLoop()
        if __name__=="__main__":main()



        


