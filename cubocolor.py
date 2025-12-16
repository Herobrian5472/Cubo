import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

COLORES = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),    
)

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

SUPERFICIES = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

def Cubo():
    glBegin(GL_QUADS)
    for superficie in SUPERFICIES:
        cmp = 0
        for vertice in superficie:
            cmp+=1
            glColor3fv(COLORES[cmp])
            glVertex3fv(VERTICES[vertice])
    glEnd()
    
    glBegin(GL_LINES)
    for arista in ARISTAS:
        for vertice in arista:
            glVertex3fv(VERTICES[vertice])
    glEnd()
    
pygame.init()
display = (800,800)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslate(0.0,0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Cubo()
    pygame.display.flip()
    pygame.time.wait(10)