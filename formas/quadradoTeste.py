import glfw
from OpenGL.GL import*
from PIL import Image


def inicializar():
    glClearColor(0.3, 0.0, 0.0, 1.0) # cor de fundo, é glClearColor especificamente

def render():
    glClear(GL_COLOR_BUFFER_BIT)

def quadrado():
    # os vertices desse rapaz precisa seguir uma ordem especifica
    verticesDoQuadrado = [
        [-0.5, 0.5], # sup esquerdo
        [-0.5, 0], # inf esquerdo
        [0.5, 0], # inf direito
        [0.5, 0.5] # sup direito
    ]

    glColor4f(0.0, 0.0, 1, 1)
    glBegin(GL_QUADS) # comecar a fazer o rapaz
    for quadVertex in verticesDoQuadrado:
        glVertex2fv(quadVertex)
    glEnd()

def main():
    glfw.init()
    window = glfw.create_window(800, 600, "Janela Quadrado", None, None)
    iconeQuadrado = "iconeQuadrado.png"
    glfw.set_window_icon(window, 1, Image.open(iconeQuadrado))

    glfw.make_context_current(window)
    inicializar()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        quadrado()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == '__main__':
    main()