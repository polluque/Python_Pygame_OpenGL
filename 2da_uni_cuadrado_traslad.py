#"""
#triangulo y ejes 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices_lineas = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
)

bordes_lineas = (
    (0, 1),
    (0, 2),
    (1, 2),
)

vertices_relleno = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
)

bordes_relleno = (
    (0, 1, 2),
)

color_fondo = (0.2, 0.3, 0.5)

class OGL:
    @staticmethod
    def three_func(a, b, func):
        return func(a[0], b[0]), func(a[1], b[1]), func(a[2], b[2])

class GLCamera:
    def __init__(self):
        self.pos = [0.0, 0.0, 5.0]
        self.rot = [0.0, 0.0, 0.0]
        self.mouse_pos = [0, 0]

    def add_to_scene(self):
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

    def change_of_basis(self):
        c = np.cos(self.rot[1] * (np.pi / 180))
        s = np.sin(self.rot[1] * (np.pi / 180))
        m1 = np.array([[c, 0, 5], [0, 1, 0], [-5, 0, c]])
        c = np.cos(self.rot[0] * (np.pi / 180))
        s = np.sin(self.rot[0] * (np.pi / 180))
        m2 = np.array([[1, 0, 0], [0, c, -s], [0, 5, c]])
        m = m1.dot(m2)
        return m

    def handle_camera_events(self, event):
        if event.type == pygame.KEYDOWN:
            cb = self.change_of_basis()
            if event.key == pygame.K_RIGHT:
                m = cb.dot(np.array([-0.5, 0, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_LEFT:
                m = cb.dot(np.array([0.5, 0, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_UP:
                m = cb.dot(np.array([0, -0.5, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_DOWN:
                m = cb.dot(np.array([0, 0.5, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)

def TrianguloLineas():
    glBegin(GL_LINES)
    for edge in bordes_lineas:
        for vertex in edge:
            glVertex3fv(vertices_lineas[vertex])
    glEnd()

def TrianguloRelleno():
    glBegin(GL_TRIANGLES)
    for edge in bordes_relleno:
        for vertex in edge:
            glColor3fv(color_fondo)
            glVertex3fv(vertices_relleno[vertex])
    glEnd()

def Ejes():
    # Eje X
    glColor3fv((1, 0, 0))
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)  # Extremo del eje X
    glEnd()
    # Eje Y
    glColor3fv((0, 1, 0))
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2, 0)  # Extremo del eje Y
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    camera = GLCamera()

    while True:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        camera.add_to_scene()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            camera.handle_camera_events(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        TrianguloRelleno()
        TrianguloLineas()
        Ejes()
        pygame.display.flip()
        pygame.time.wait(10)

main()
#""" 

"""
#triangulo con color 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices_lineas = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
)

bordes_lineas = (
    (0, 1),
    (0, 2),
    (1, 2),
)

vertices_relleno = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
)

bordes_relleno = (
    (0, 1, 2),
)

color_fondo = (0.2, 0.3, 0.5)

class OGL:
    @staticmethod
    def three_func(a, b, func):
        return func(a[0], b[0]), func(a[1], b[1]), func(a[2], b[2])

class GLCamera:
    def __init__(self):
        self.pos = [0.0, 0.0, 5.0]
        self.rot = [0.0, 0.0, 0.0]
        self.mouse_pos = [0, 0]

    def add_to_scene(self):
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

    def change_of_basis(self):
        c = np.cos(self.rot[1] * (np.pi / 180))
        s = np.sin(self.rot[1] * (np.pi / 180))
        m1 = np.array([[c, 0, 5], [0, 1, 0], [-5, 0, c]])
        c = np.cos(self.rot[0] * (np.pi / 180))
        s = np.sin(self.rot[0] * (np.pi / 180))
        m2 = np.array([[1, 0, 0], [0, c, -s], [0, 5, c]])
        m = m1.dot(m2)
        return m

    def handle_camera_events(self, event):
        if event.type == pygame.KEYDOWN:
            cb = self.change_of_basis()
            if event.key == pygame.K_RIGHT:
                m = cb.dot(np.array([-0.5, 0, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_LEFT:
                m = cb.dot(np.array([0.5, 0, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_UP:
                m = cb.dot(np.array([0, -0.5, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_DOWN:
                m = cb.dot(np.array([0, 0.5, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)

def TrianguloLineas():
    glBegin(GL_LINES)
    for edge in bordes_lineas:
        for vertex in edge:
            glVertex3fv(vertices_lineas[vertex])
    glEnd()

def TrianguloRelleno():
    glBegin(GL_TRIANGLES)
    for edge in bordes_relleno:
        for vertex in edge:
            glColor3fv(color_fondo)
            glVertex3fv(vertices_relleno[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    camera = GLCamera()

    while True:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        camera.add_to_scene()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            camera.handle_camera_events(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        TrianguloRelleno()
        TrianguloLineas()
        pygame.display.flip()
        pygame.time.wait(10)

main()
"""



"""
#triangulo alambrado
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
)

bordes = (
    (0, 1),
    (0, 2),
    (1, 2),
)

class OGL:
    @staticmethod
    def three_func(a, b, func):
        return func(a[0], b[0]), func(a[1], b[1]), func(a[2], b[2])

class GLCamera:
    def __init__(self):
        self.pos = [0.0, 0.0, 5.0]
        self.rot = [0.0, 0.0, 0.0]
        self.mouse_pos = [0, 0]

    def add_to_scene(self):
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

    def change_of_basis(self):
        c = np.cos(self.rot[1] * (np.pi / 180))
        s = np.sin(self.rot[1] * (np.pi / 180))
        m1 = np.array([[c, 0, 5], [0, 1, 0], [-5, 0, c]])
        c = np.cos(self.rot[0] * (np.pi / 180))
        s = np.sin(self.rot[0] * (np.pi / 180))
        m2 = np.array([[1, 0, 0], [0, c, -s], [0, 5, c]])
        m = m1.dot(m2)
        return m

    def handle_camera_events(self, event):
        if event.type == pygame.KEYDOWN:
            cb = self.change_of_basis()
            if event.key == pygame.K_RIGHT:
                m = cb.dot(np.array([-0.5, 0, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_LEFT:
                m = cb.dot(np.array([0.5, 0, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_UP:
                m = cb.dot(np.array([0, -0.5, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_DOWN:
                m = cb.dot(np.array([0, 0.5, 0]))
                self.pos = OGL.three_func(self.pos, m, lambda x, y: x + y)

def Triangulo():
    glBegin(GL_LINES)
    for edge in bordes:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    camera = GLCamera()

    while True:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        camera.add_to_scene()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            camera.handle_camera_events(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Triangulo()
        pygame.display.flip()
        pygame.time.wait(10)

main()
"""



"""
#cuadrado alambrado
import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*
import numpy as np

#conjuntos en python 
vertices = (   
    (-1,1,0),
    (-1,-1,0),
    (1,-1,0),
    (1,1,0),
    (-1,-1,0),
    )

bordes = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3)
    )

'''class auto():
    def __init__(self,pmodelo,pmarca): 
        self.modelo=pmodelo
        self.marca =pmarca

a1=auto()
print(a1.modelo)'''

class OGL():
    def three_func(a,b,func):
        return(func(a[0],b[0]),func(a[1],b[1]),func(a[2],b[2]))

class GLCamera():
    def __init__(self):
        self.pos =[0.0,0.0,10.0]
        self.rot=[0.0,0.0,0.0]
        self.rotating = False
        self.mouse_pos=[0,0]

    def add_to_scene(self):
        glTranslatef(-self.pos[0],-self.pos[1],-self.pos[2]);
    
    def change_of_basis(self):
        c=np.cos(self.rot[1]*(np.pi/180)) 
        s=np.sin(self.rot[1]*(np.pi/180)) 
        m1=np.array([[c,0,5], [0,1,0], [-5,0, c]]) 
        c=np.cos(self.rot[0]*(np.pi/180)) 
        s=np.sin(self.rot[0]*(np.pi/180)) 
        m2=np.array([[1,0,0], [0,c, -s], [0, 5, c]])
        m=m1.dot(m2) 
        return m
    
    def handle_camera_events(self,event): 
        if event.type == pygame.KEYDOWN: 
            cb = self. change_of_basis() 
            if event.key == pygame.K_RIGHT: 
                m=cb.dot(np.array([-0.5,0,0])) 
                self.pos=OGL.three_func(self.pos,m, lambda x,y : x+y ) 
            if event.key == pygame.K_LEFT: 
                m=cb.dot(np.array([0.5,0,0])) 
                self.pos=OGL.three_func(self.pos,m, lambda x, y : x+y ) 
            if event.key == pygame.K_UP: 
                m=cb.dot(np.array([0,-0.5,0])) 
                self.pos=OGL.three_func(self.pos,m, lambda x, y : x+y ) 
            if event.key == pygame.K_DOWN: 
                m=cb.dot(np.array([0,0.5,0])) 
                self.pos=OGL.three_func(self.pos,m, lambda x, y : x+y )
    
    
def Cuadrado(): 
    glBegin(GL_LINES) 
    for edge in bordes: 
        for vertex in edge: 
            glVertex3fv(vertices[vertex]) 
    glEnd ()

def main():
    pygame. init() 
    display = (800,600) 
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL) 
    camera = GLCamera()
    
    while True:
        glMatrixMode(GL_MODELVIEW) 
        glLoadIdentity() 
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) 
        camera.add_to_scene() 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : 
                pygame.quit() 
                quit() 
            camera.handle_camera_events(event)
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
        Cuadrado() 
        pygame.display.flip() 
        pygame.time.wait (10) 

main()
"""