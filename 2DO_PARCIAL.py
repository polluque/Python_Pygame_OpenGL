#segunda pregunta 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def tex_coord(x, y, n=4):
    """
    Return the bounding vertices of the texture square.
    """

    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m

def tex_coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and
    side.
    """
    top = tex_coord(*top)
    bottom = tex_coord(*bottom)
    side = tex_coord(*side)
    result = [
                (top),
                (bottom),
                (side),
                (side),
                (side),
                (side),
             ]
    """result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)"""
    return result

#block type names and location on template go here
BLOCK1 = tex_coords((3, 0), (3, 0), (3, 0))

def verts(x, y, z, n):
    vertices = (
    (1+(2*x), -1+(2*y), -1+(2*z)),
    (1+(2*x), 1+(2*y), -1+(2*z)),
    (-1+(2*x), 1+(2*y), -1+(2*z)),
    (-1+(2*x), -1+(2*y), -1+(2*z)),
    (1+(2*x), -1+(2*y), 1+(2*z)),
    (1+(2*x), 1+(2*y), 1+(2*z)),
    (-1+(2*x), -1+(2*y), 1+(2*z)),
    (-1+(2*x), 1+(2*y), 1+(2*z))
    )
    return(vertices)
print(verts(0, 0, 0, 1))


edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
colors = (

    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )
forced = False

def Cube(vx,vy,vz,block):
    if not forced:
        glBegin(GL_QUADS)
        y = 0
        for surface in surfaces:
            x = 0
            y+=1
            for vertex in surface:
                x+=1
                #glColor3fv(colors[x])
                glTexCoord2f(block[y-1][2*(x-1)], block[y-1][(2*x)-1])
                #print(block[y-1][2*(x-1)], block[y-1][(2*x)-1])
                glVertex3fv(verts(vx,vy,vz,1)[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verts(vx,vy,vz,1)[vertex])
        glEnd()
    else:
        texX = 0.75
        texY = 0.25
        glBegin(GL_QUADS)
        glTexCoord2f(0.0+texX, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(0.25+texX, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(0.25+texX, 0.25)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0+texX, 0.25)
        glVertex3f(-1.0, 1.0, 1.0)
        glEnd()

def loadTexture():
    textureSurface = pygame.image.load('ladrillo.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    
    glColor3f(0.5, 0.5, 0.5)
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
    0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

    glDisable(GL_TEXTURE_2D)


pygame.init()
display = (800, 600)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])
"""
glClearColor(0.0, 0.0, 0.0, 0.0)
glClearDepth(1.0)
glDepthMask(GL_TRUE)
glDepthFunc(GL_LESS)
glEnable(GL_DEPTH_TEST)
#glEnable(GL_CULL_FACE)
#glCullFace(GL_FRONT)
##glFrontFace(GL_CCW)
##glShadeModel(GL_SMOOTH)
glDepthRange(0.0,1.0)
"""
sphere = gluNewQuadric()
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()
# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

loadTexture()
up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)
            if not paused:
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                    
                    pygame.mouse.set_pos(displayCenter)
    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        #mouseMove = pygame.mouse.get_rel()
        # init model view matrix
        glLoadIdentity()
        # apply the look up and down
        up_down_angle += mouseMove[1]*0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)
        # init the view matrix
        glPushMatrix()
        glLoadIdentity()
        # apply the movment
        if keypress[pygame.K_w]:
            glTranslatef(0,0,0.1)
        if keypress[pygame.K_s]:
            glTranslatef(0,0,-0.1)
        if keypress[pygame.K_d]:
            glTranslatef(-0.1,0,0)
        if keypress[pygame.K_a]:
            glTranslatef(0.1,0,0)
        if keypress[pygame.K_LSHIFT]:
            glTranslatef(0,0.5,0)

        if keypress[pygame.K_SPACE]:
            glTranslatef(0,-0.5,0)
        # apply the left and right rotation
            glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)
            # multiply the current matrix by the get the new view matrix and store the final vie matrix
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
            # apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)
            #glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            glEnable(GL_TEXTURE_2D)
            Cube(0,0,0,BLOCK1)
            Cube(1,0,0,BLOCK1)
            Cube(0,1,0,BLOCK1)
            Cube(0,0,1,BLOCK1)
            Cube(-2,0,0,BLOCK1)
            glDisable(GL_TEXTURE_2D)
            glColor4f(0.5, 0.5, 0.5, 1)
            glBegin(GL_QUADS)
            glVertex3f(-10, -10, -2)
            glVertex3f(10, -10, -2)
            glVertex3f(10, 10, -2)
            glVertex3f(-10, 10, -2)
            glEnd()
            glTranslatef(-1.5, 0, 0)
            glColor4f(0.5, 0.2, 0.2, 1)
            gluSphere(sphere, 1.0, 32, 16)
            glTranslatef(3, 0, 0)
            glColor4f(0.2, 0.2, 0.5, 1)
            gluSphere(sphere, 1.0, 32, 16)
            glColor3f(1, 1, 1)
            glPopMatrix()
            pygame.display.flip()
            pygame.time.wait(10)

pygame.quit()
"""
#primera pregunta 

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