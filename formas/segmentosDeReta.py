import glfw
from OpenGL.GL import *
from PIL import Image

def inicializar():
    glClearColor(1, 1, 1, 1)
    glLineWidth(20)

def render():
    glClear(GL_COLOR_BUFFER_BIT)

def segmentosDeReta():
    # novamente, precisa ter pares, eu to so colocando uns pontos e eles se conectam

    vertices = [
    
    [-0.5, -0.5],
    [-0.5, 0.5],
    [0.5, -0.5],
    [0.5, 0.5],
    [0.0, 0.3] # veja que esse camarada n vai se conectar com o resto
    
    
    ]

    cores = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0.5, 0.3, 0.2]
         
    ]

    glBegin(GL_LINES) # essa função so se conecta com PARES
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()


def segmentosDeRetaQueSeConectam():
    vertices = [
    
    [-0.5, -0.5],
    [-0.5, 0.5],
    [0.0, 0.1], # pra ficar no meio
    [0.5, 0.5],
    [0.5, -0.5]
    
    ]

    cores = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0.5, 0.3, 0.2]
         
    ]

    glBegin(GL_LINE_STRIP) # essa função conecta todo mundo
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()


def main():
    glfw.init()
    window = glfw.create_window(800, 600, "Segmentos de reta", None, None)
    Jinx = "Jinx.jpg"
    glfw.set_window_icon(window, 1, Image.open(Jinx))

    glfw.make_context_current(window)
    inicializar()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        #segmentosDeReta()
        segmentosDeRetaQueSeConectam()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == '__main__':
    main()


