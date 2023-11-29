#importacion de librerias 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from PIL import Image
#definir una funcion para la carga de textura usando pillow 
def load_texture(file_path):
    # Cargar la imagen de textura usando PIL
    img = Image.open(file_path)
    img_data = img.tobytes()

    # Obtener las dimensiones de la imagen
    width, height = img.size

    # Crear una textura
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Configurar la textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    return texture_id

#creacion y definicion del tamaño de la ventana 
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

# carga de textura
planet_texture = load_texture("textura_azul.jpg")

#configuracion de la matriz de proyeccion 
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
#definicion de teclas para el manejo de la camara
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
    glMaterialfv(GL_FRONT, GL_SHININESS, 100.0)

    # Definir posición de luz
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])
    #glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, 0, -1])  # Puedes ajustar estos valores

    # Dibujar el sol
    glPushMatrix()
    glTranslatef(0, 0, 0)
    gluSphere(planet1, 0.3, 32, 16)  # se puede hacer cambios en el tamaño del sol 
    glPopMatrix()

    # Dibujar planetas
    for i, (x, y, z) in enumerate(planet_positions):
        glPushMatrix()
        glTranslatef(x, y, z)
        if i == 1:  # Aplicar textura solo al segundo planeta
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, planet_texture)
            gluQuadricTexture(planet2, True)
            gluSphere(planet2, planet_sizes[i], 32, 16)
            glDisable(GL_TEXTURE_2D)
        else:
            #glColor4f(0.0, 1.0, 0.0, 0.0)
            gluSphere([planet1, planet2, planet3][i], planet_sizes[i], 32, 16)
        glPopMatrix()

        # Rotacion d e los  planetas alrededor de su propio eje
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
import sys
import math 
from OpenGL.GL import* 
from OpenGL.GLU import* 
from OpenGL.GLUT import*

#Iluminacion
class Luz(object): 
    encendida=True 
    colores=[(1.,1., 1., 1.), (1., 0.5, 0.5,1.), 
             (0,5,1., 0.5,1.),(0, 5, 0.5,1., 1. )] 
    def __init__(self, luz_id,posicion): 
        self.luz_id=luz_id 
        self.posicion=posicion 
        self.color_actual=0
#Iluminacion
    def iluminar(self): 
        light_id=self.luz_id 
        color=Luz.colores[self.color_actual] 
        glLightfv(light_id, GL_POSITION, self.posicion) 
        glLightfv(light_id,GL_DIFFUSE, color) 
        glLightfv(light_id,GL_CONSTANT_ATTENUATION,0.1) 
        glLightfv(light_id, GL_LINEAR_ATTENUATION,0.05) 
    def cambiar_color(selft): 
        selft.color_actual+=1 
        selft.color_actual%=len(Luz.colores)
    def enable(self):
        if not Luz.encendida: 
            glEnable(GL_LIGHTING) 
            Luz. encendida=True 
            glEnable(self.luz_id)
#Construccion de la esfera
class Esfera(object):
    meridiano=40
    paralelos=40 #Constructor
    def __init__(self,radio,posicion, color): 
        self.radio=radio 
        self.posicion=posicion 
        self.color=color
    # Dibujar la esfera 
    def dibujar(self): 
        glTranslatef(*self.posicion) 
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.color) 
        glutSolidSphere(self.radio, Esfera.meridiano, Esfera.paralelos)

# -Sistema Planetario-
class Planetario(object): 
    def __init__(self, largo=800, ancho=600): 
        self.titulo='Sistema planetario' 
        self.largo=largo 
        self.ancho=ancho 
        self.angulo=0 
        self.distancia=20 
        self.iluminacion=Luz(GL_LIGHT0,(15,5,15,1)) 
        #crear la esfera 
        self.esfera=Esfera(2,(0,0,0),(1,1,0,1)) 
    
    def iniciar(self): 
        glutInit() 
        glutInitDisplayMode(GLUT_DOUBLE |GLUT_DEPTH) 
        glutInitWindowPosition(50,50) 
        glutInitWindowSize(self.largo, self.ancho)

        glutCreateWindow(self. titulo) 
        glEnable(GL_DEPTH_TEST) 
        glEnable(GL_LIGHTING) 
        glEnable(GL_LIGHT0) 
        self.iluminacion.enable 
        glClearColor(.1,.1,.1,1) 
        glMatrixMode (GL_PROJECTION) 
        aspect=self. largo/self.ancho 
        gluPerspective(40.,aspect,1.,40.) 
        glMatrixMode(GL_MODELVIEW) 
        glutDisplayFunc(self.dibujar) 
        glutSpecialFunc(self.keyboard) 
        glutMainLoop() 
    def dibujar(self): 
    #Cordenadas polares 
        x=math.sin(self.angulo)*self.distancia 
        Z=math.cos(self.angulo)*self.distancia
    
        glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT) 
        glLoadIdentity() 
        gluLookAt(x,0,Z,0,0,0,0,1,0)
        self. iluminacion.iluminar()
        self.esfera.dibujar()
        glutSwapBuffers() 
    def keyboard(self,tecla,x,y): 
        if tecla == GLUT_KEY_INSERT: 
            sys.exit()
        if tecla == GLUT_KEY_UP:    
            self.distancia -= 0.1
        if tecla == GLUT_KEY_DOWN: 
            self.distancia+=0.1 
        if tecla == GLUT_KEY_LEFT: 
            self.angulo -= 0.05
        if tecla == GLUT_KEY_RIGHT: 
            self.angulo+=0.05 
        if tecla == GLUT_KEY_F1: 
            self. iluminacion. cambiar_color() 
        self.distancia=max(10,min(self.distancia,20)) 
        self.angulo%=math.pi*2 
        glutPostRedisplay()
# ---- Principal ----
if __name__=='__main__': 
        Aplicar=Planetario() 
        Aplicar. iniciar()
        """