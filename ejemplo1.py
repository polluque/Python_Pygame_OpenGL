from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)


glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
glutCreateWindow("Primera ventana en OpenGl")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()


