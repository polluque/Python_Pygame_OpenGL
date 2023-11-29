#importando librerias y asignando alias 
import OpenGL.GL as gl
import pygame
import sys

# configurando el tamaño de la ventana
window_size = (600, 600)

def plot_circle(xc, yc, x, y):
    #  se dibuja puntos en los 8 octantes 
    gl.glVertex2f(xc + x, yc + y)
    gl.glVertex2f(xc - x, yc + y)
    gl.glVertex2f(xc + x, yc - y)
    gl.glVertex2f(xc - x, yc - y)
    gl.glVertex2f(xc + y, yc + x)
    gl.glVertex2f(xc - y, yc + x)
    gl.glVertex2f(xc + y, yc - x)
    gl.glVertex2f(xc - y, yc - x)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r # radio de la circunferencia 
    p = 1 - r  # decide si recorrer a derecha o a la izquierda, dibujando puntos 

    # Configurar ventana de salida 
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT) #limpieza del buffer por si hubo otro dibujo 
    gl.glPointSize(1) #tamaño de los puntos 
    gl.glColor3f(1.0, 1.0, 1.0) # color de los puntos 

    gl.glBegin(gl.GL_POINTS)#funcion de dibujo de los puntos 

    # Dibuja el primer punto en el octante superior derecho
    plot_circle(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle(xc, yc, x, y)

    gl.glEnd()
    gl.glFlush()

def main():
    pygame.init()
    pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Circunferencia con Algoritmo de Punto Medio")

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(0, window_size[0], 0, window_size[1], -1, 1)

    xc, yc, r = window_size[0] // 2, window_size[1] // 2, 200  # Coordenadas del centro y radio

    midpoint_circle(xc, yc, r)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
