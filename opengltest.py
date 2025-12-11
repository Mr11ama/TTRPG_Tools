import pygame
from pygame.locals import *
import math as m

from OpenGL.GL import *
from OpenGL.GLU import *

phi = (1+m.sqrt(5))/2
tilt_offset = m.degrees(m.atan(1/2))

def Rx(v,angle):
    new_y = m.cos(angle)*v[1] - m.sin(angle)*v[2]
    new_z = m.sin(angle)*v[1] + m.cos(angle)*v[2]
    return (v[0], new_y, new_z)

#def Ry(v,angle):

verticies = [
    [0, -phi, 1],
    [0, phi, 1],
    [0, phi, -1],
    [0, -phi, -1],
    [1, 0, phi],
    [-1, 0, phi],
    [-1, 0, -phi],
    [1, 0, -phi],
    [phi, 1, 0],
    [-phi, 1, 0],
    [-phi, -1, 0],
    [phi, -1, 0],
    ]

for i in range(len(verticies)):
    verticies[i] = Rx(verticies[i], m.tan(1/2))

print(verticies)

edges = (
    (0, 5),
    (0, 4),
    (0, 11),
    (0, 3),
    (0, 10),
    (4, 5),
    (4, 1),
    (4, 8),
    (4, 11),
    (5, 1),
    (5, 9),
    (5, 10),
    (8, 11),
    (8, 2),
    (8, 7),
    (7, 2),
    (7, 3),
    (7, 6),
    (7, 11),
    (6, 2),
    (6, 9),
    (6, 3),
    (6, 10),
    (10, 3),
    (10, 9),
    (9, 1),
    (9, 2),
    (2, 1),
    (1, 8),
    (3, 11))



def Icosahedron():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.25,0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Icosahedron()
        pygame.display.flip()
        pygame.time.wait(10)


main()