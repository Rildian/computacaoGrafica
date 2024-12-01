import glfw
from OpenGL.GL import*
from PIL import Image

point = [0, 0]
veloc = 0.2
angulo = 0 
teclas = {
        glfw.KEY_W: False,
        glfw.KEY_A: False,
        glfw.KEY_S: False,
        glfw.KEY_D: False,
        glfw.KEY_SPACE: False
    }

def inicializar():
    glClearColor(1, 1, 1, 1)
    glPointSize(15)
    glLineWidth(5)

def teclado(window, key, scancode, action, mods):
    global teclas
    if action == glfw.PRESS:
        teclas[key] = True
    elif action == glfw.RELEASE:
        teclas[key] = False
    
    if action == glfw.REPEAT and teclas[glfw.KEY_D]:
        print("Solte o D pai")

def seMova():           
    global teclas, angulo
    if teclas[glfw.KEY_W]:
        point[1] += veloc
    if teclas[glfw.KEY_S]:
        point[1] -= veloc
    if teclas[glfw.KEY_A]:
        point[0] -= veloc
    if teclas[glfw.KEY_D]:
        point[0] += veloc
    if teclas[glfw.KEY_SPACE]: 
        angulo += 0

def render():
    global angulo
    angulo += 0.05
    glClear(GL_COLOR_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)       
    glLoadIdentity()                                        
    glRotatef(angulo, 1, 0, 1)                                           
    nave()

def nave():
    vertices = [
        [-0.5, 0.0],
        [0.0, 0.0],
        [0.0, -0.5],
        [0.5, 0.5]
    ]

    cores = [
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0]
    ]

    glBegin(GL_LINE_LOOP)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()


def main():
    glfw.init()
    window = glfw.create_window(800, 600, "He knows... it's over", None, None)
    foto = "ItsOver.jpeg"
    glfw.set_window_icon(window, 1, Image.open(foto))
    
    glfw.make_context_current(window)
    glfw.set_key_callback(window, teclado)
    inicializar()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        seMova()
        render()

        glfw.swap_buffers(window)
    glfw.terminate()

    
if __name__ == '__main__':
    main()

