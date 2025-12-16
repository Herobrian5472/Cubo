import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

VERTICES = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

ARISTAS = (
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

def Cubo():
    glBegin(GL_LINES)
    for arista in ARISTAS:
        for vertice in arista:
            glVertex3fv(VERTICES[vertice])
    glEnd()
    
pygame.init()
ZONA = (800,800)
pygame.display.set_mode(ZONA, pygame.DOUBLEBUF|pygame.OPENGL)

gluPerspective(45, (ZONA[0]/ZONA[1]), 0.1, 50.0)
glTranslate(0.0,0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    glRotatef(1, 3, 1, 3)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cubo()
    pygame.display.flip()
    pygame.time.wait(10)
    
    
# para correrlo en la terminal linux

#source ~/venvs/pygame/bin/activate
#python /home/briangallardo/Escritorio/Python\ proyectos/cubo/cubo.py

#esas dos lineas juntas sin los # corren el cubo.py