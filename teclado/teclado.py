import glfw
from OpenGL.GL import *

point = [0, 0]
veloc = 0.0002
keys = {
    glfw.KEY_A: False,
    glfw.KEY_D: False,
    glfw.KEY_S: False,
    glfw.KEY_W: False,
}

# FunÃ§Ã£o contendo as configuraÃ§Ãµes iniciais da minha aplicaÃ§Ã£o
def initialize():
    glClearColor(1,1,1,1)   # define a cor que serÃ¡ usada para limpar a imagem
    glPointSize(20)         # define o tamanho dos pontos

def movePoint():
    global point
    if keys[glfw.KEY_A]: point[0] -= veloc
    if keys[glfw.KEY_D]: point[0] += veloc
    if keys[glfw.KEY_S]: point[1] -= veloc
    if keys[glfw.KEY_W]: point[1] += veloc

# callback function pressionar de uma tecla
def keyboard(window, key, scancode, action, mods):
    global keys
    if action == glfw.PRESS:     
        keys[key] = True
    elif action == glfw.RELEASE: keys[key] = False

def update():
    movePoint()

# FunÃ§Ã£o usada para atualizar o desenho da tela
def render():
    glClear(GL_COLOR_BUFFER_BIT)    # atribui a cor definida em glClearColor a todos os pixels

    glBegin(GL_POINTS)              # a primitiva a ser desenhada Ã© ponto
    glColor3f(1,0,0)                # define que a cor de desenho serÃ¡ vermelha
    glVertex2fv(point)                 
    glEnd()

# FunÃ§Ã£o principal
def main():
    glfw.init()                                                   # inicializa GLFW
    window = glfw.create_window(500,500,'03 - Teclado', None, None) # criando a janela
    glfw.make_context_current(window)                             # atribuindo um contexto OpenGL a janela
    glfw.set_key_callback(window,keyboard)
    initialize()                                                  # funÃ§Ã£o com minhas configuraÃ§Ãµes iniciais
    while not glfw.window_should_close(window):                   # laÃ§o principal
        glfw.poll_events()                                        # tratamento de entrada
        update()
        render()                                                  # funÃ§Ã£o com atualizaÃ§Ã£o do desenho
        glfw.swap_buffers(window)                                 # troca frame buffer exibido na tela (double buffering)
    glfw.terminate()                                              # finaliza GLFW

if __name__ == '__main__':
    main()