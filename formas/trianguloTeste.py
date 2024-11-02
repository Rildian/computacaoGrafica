import glfw
from OpenGL.GL import*
from PIL import Image # biblioteca p/ ícones

def inicializar():
    glClearColor(0.0, 0.0, 0.3, 1.0) # cor que vai ser usada de fudo

def triangulo():
    verticesDoTriangulo = [
        [-0.5, 0],
        [0.5, 0],
        [0, 0.5]
    ]

    glColor(1, 0, 0, 1) # cores RGB
    glBegin(GL_TRIANGLES) # comece a desenhar o triangulo
    for vertex in verticesDoTriangulo:
        glVertex2fv(vertex) # aqui as coordenadas do triangulo
    glEnd()

def render():
    glClear(GL_COLOR_BUFFER_BIT) # limpe a memoria da placa de video pra mostrar o meu desenho :)

def main():
    glfw.init()
    window = glfw.create_window(800, 600, "Janela Triangulo", None, None) # larguraxaltura, nome e o resto
    icone = "icone.jpg" # assim que configura o icone, precisa ta no mesmo diretorio
    glfw.set_window_icon(window, 1, Image.open(icone)) # setando o icone, precisa da jannela, quantidade de icones e o proprio icone

    glfw.make_context_current(window)
    inicializar()
    
    while not glfw.make_context_current(window):
        glfw.poll_events()
        render()
        triangulo()
        glfw.swap_buffers(window) # precisa desse parametro pai
    glfw.terminate()

if __name__ == '__main__':
    main()


