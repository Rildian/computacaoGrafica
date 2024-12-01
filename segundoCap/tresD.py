import glfw 
from OpenGL.GL import*
from OpenGL.GLU import * # importante pra parte de gluPerspective
from PIL import Image
import numpy as np

angulo = 0

def inicializar():
    glClearColor(0, 0, 0, 0)

def render():
    global angulo
    # coloque as matrizes aki
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # limpando o buffer de cor e o buffer de profundidade
    glEnable(GL_DEPTH_TEST) # pra dar profundidade
    glMatrixMode(GL_PROJECTION) # qual é a matriz atual? GL_PROjection vai aplicar mudanças a matriz subsequente
    glLoadIdentity() # substitui a matriz atual por uma de identidade
    angulo += 0.05
    glRotatef(angulo, 0.5, 1, 1)
    glScalef(0.5, 0.5, 0.5)
    piramede()
    #cubo()


def cubo():
    vertices = [
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5],
    ]
    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [2, 3, 7, 6],
        [0, 3, 7, 4],
        [1, 2, 6, 5],
    ]

    cores = [
        [1.0, 0.0, 0.0],
        [0.365, 0.427, 0.882],
        [0.490, 0.604, 0.573],
        [0.957, 0.816, 0.247],
        [0.953, 0.612, 0.071],
        [0.608, 0.349, 0.712],
        [0.740, 0.765, 0.780],
        [0.105, 0.737, 0.612]
    ]

    glBegin(GL_QUADS)
    for face in faces: # entender esses loops e faces
        for vertice in face:
            glColor3fv(cores[vertice])
            glVertex3fv(vertices[vertice])
    glEnd()


def piramede():
    vertices = [
        [0, 0, 1],
        [-1, -1, -1],
        [-1, 1, -1],
        [1, 1, -1],
        [1, -1, -1]
    ]

    faces = [
        [0, 1, 2],  
        [1, 0, 4],  
        [2, 0, 3],  
        [3, 0, 4],  
        [1, 2, 3, 4]  # base quadrada
    ]

    cores = [
        [1, 0, 0],  # vermelho no topo 
        [0, 1, 0],  
        [0, 0, 1],  
        [1, 1, 0],  
        [0, 1, 1],  # ciano na base
    ]

    glBegin(GL_TRIANGLES)
    for face in faces[:-1]: # p/ n acessar o ultimo item da lista
        for v in face: # pra cada face:
            glColor3fv(cores[v]) # coloque uma determinada cor
            glVertex3fv(vertices[v]) # desenhe um vertice
    glEnd()

    glBegin(GL_QUADS)
    for v in faces[-1]: # p/ acessar o ultimo item da lista
        glColor3fv(cores[v]) # p/ essa unica face, coloque essa cor
        glVertex3fv(vertices[v]) # p/ essa unica face, coloque esse vertice
    glEnd()


def main():
    glfw.init()
    
    window = glfw.create_window(800, 600, "3D", None, None)
    icon = "cabousse.jpeg"
    glfw.set_window_icon(window, 1, Image.open(icon))
    
    glfw.make_context_current(window)
    inicializar()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        render()
        
        
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == '__main__':
    main()

    
