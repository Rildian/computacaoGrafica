import glfw 
from OpenGL.GL import *
from PIL import Image

#infelizmente, na parte do teclado, acredito que não é capaz de fazer sem ser usando global.
#a função teclado espera exatamente aquela quatidade de parametros, n tem como eu passar
#meu dicionario
#pelo menos eu n consegui pensar numa maneira
ponto = [0,0]
veloc = 0.0002
teclas = {
        glfw.KEY_W: False,
        glfw.KEY_A: False,
        glfw.KEY_S: False,
        glfw.KEY_D: False
    }

def inicializar():
    glClearColor(1, 1, 1, 1)
    glPointSize(50)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_POINTS)              
    glColor3f(1,0,0)                
    glVertex2fv(ponto)                 
    glEnd()


def seMova():           
    global teclas 

    if teclas[glfw.KEY_W]:
        ponto[1] += veloc
    if teclas[glfw.KEY_S]:
        ponto[1] -= veloc
    if teclas[glfw.KEY_A]:
        ponto[0] -= veloc
    if teclas[glfw.KEY_D]:
        ponto[0] += veloc

def teclado(window, key, scancode, action, mods):
    global teclas
    if action == glfw.PRESS:
        teclas[key] = True  
    elif action == glfw.RELEASE:
        teclas[key] = False  

    if action == glfw.REPEAT and teclas[glfw.KEY_D]:  
        print("Solta a porra desse D")


def main():
    glfw.init()
    window = glfw.create_window(800, 600, "Com o teclado pae", None, None)
    icon = "2pac.jpg"
    glfw.set_window_icon(window, 1, Image.open(icon))
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