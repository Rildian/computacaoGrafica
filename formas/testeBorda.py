import glfw 
from OpenGL.GL import *
from PIL import Image

def inicializar():
    glClearColor(1, 1, 1, 1) 
    glLineWidth(5)
    glPointSize(20)

def render():
    glClear(GL_COLOR_BUFFER_BIT)

def quadradoComBorda():
    verticesDoQuadrado = [
        [-0.5, -0.5],
        [-0.5, 0.5],
        [0.5, 0.5],

        [0.5, -0.5],
        [-0.5, -0.5],
        [-0.5, 0.5]
    ]

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.498, 0.996)
    for v in verticesDoQuadrado:
        glVertex2fv(v)
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    for v in verticesDoQuadrado:
        glVertex2fv(v)
    glEnd()


def main():
    glfw.init()
    window = glfw.create_window(800, 600, "Lista", None, None)
    foto = "foto.png"
    glfw.set_window_icon(window, 1, Image.open(foto))

    glfw.make_context_current(window)
    inicializar()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        quadradoComBorda()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == '__main__':
    main()