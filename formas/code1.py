import glfw
from OpenGL.GL import *
from math import sin, cos, radians

# FunÃ§Ã£o contendo as configuraÃ§Ãµes iniciais da minha aplicaÃ§Ã£o
def initialize():
    glClearColor(1,1,1,1)   # define a cor que serÃ¡ usada para limpar a imagem
    glPointSize(10)         # define o tamanho dos pontos
    glLineWidth(5)          # define a largura dos segmentos de reta

# FunÃ§Ã£o que desenha 4 pontos com cores diferentes na tela
def pontos():
    vertices = [        # lista das coordenadas dos vÃ©rtices
        [-0.5,-0.5],
        [ 0.5,-0.5],
        [ 0.5, 0.5],
        [-0.5, 0.5],
    ]
    cores = [           # lista das cores dos vÃ©rtices
        [1,0,0],
        [0,1,0],
        [0,0,1],
        [1,0,1],
    ]
    
    glBegin(GL_POINTS)  # primitiva: pontos
    for v, c in zip(vertices, cores):
        glColor3fv(c)   # cor de cada vÃ©rtice
        glVertex2fv(v)  # coordenada de cada vÃ©rtice
    glEnd()

# FunÃ§Ã£o que desenha 3 segmentos de reta com cores diferentes na tela
def segmentosDeReta():
    vertices = [        # lista de coordenadas dos vÃ©rtices
        [-0.5, 0.0],
        [ 0.0, 0.5],
        [-0.5,-0.5],
        [ 0.5, 0.5],
        [ 0.0,-0.5],
        [ 0.5, 0.0],
    ]
    cores = [           # lista de cores dos vÃ©rtices
        [1,1,0],
        [0,1,1],
        [0,1,1],
        [0,1,1],
        [1,0,1],
        [1,0,1],
    ]
    
    glBegin(GL_LINES)   # primitiva: segmentos de reta (conecta em pares)
    for v, c in zip(vertices, cores):
        glColor3fv(c)   
        glVertex2fv(v)
    glEnd()

# FunÃ§Ã£o que desenha uma sÃ©rie de segmentos de reta conectados em sequÃªncia
def linhaConectada():
    vertices = [        
        [-0.5,-0.5],
        [-0.5, 0.5],
        [ 0.0,-0.2],
        [ 0.5, 0.5],
        [ 0.5,-0.5],
    ]
    cores = [
        [1.0,0.0,0.0],
        [0.5,0.0,0.0],
        [0.0,0.0,0.0],
        [0.5,0.0,0.0],
        [1.0,0.0,0.0],
    ]
    
    glBegin(GL_LINE_STRIP)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

# FunÃ§Ã£o que desenha dois triÃ¢ngulos na tela
def triangulos(borda = True):
    vertices = [
        [-0.8,-0.6],
        [ 0.0,-0.6],
        [-0.4, 0.6],
        [ 0.0, 0.6],
        [ 0.4,-0.6],
        [ 0.8, 0.6],
    ]
    cores = [
        [0.5,0.0,0.0],
        [0.5,0.0,0.0],
        [0.5,0.0,0.0],
        [0.0,0.5,0.0],
        [0.0,0.5,0.0],
        [0.0,0.5,0.0],
    ]
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)       # habilitando a renderizaÃ§Ã£o de polÃ­gonos de forma preenchida
    glBegin(GL_TRIANGLES)                           # primitiva: triÃ¢ngulos (conecta de trÃªs em trÃªs)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

    if borda:                                       # caso deseje visualizar as bordas dos polÃ­gonos na cor preta
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)   # habilitando a rasterizaÃ§Ã£o apenas das arestas dos polÃ­gonos
        glColor3f(0,0,0)                            # atribuindo uma cor uniforme para todos os vÃ©rtices
        glBegin(GL_TRIANGLES)
        for v in vertices:
            glVertex2fv(v)
        glEnd()

# FunÃ§Ã£o que desenha vÃ¡rios triÃ¢ngulos conectados em sequÃªncia
def triangulosConectados(borda=True):
    vertices = [
        [-0.5,-0.5],
        [-0.5, 0.5],
        [ 0.0,-0.5],
        [ 0.0, 0.5],
        [ 0.5,-0.5],
        [ 0.5, 0.5],
    ]
    cores = [
        [1.0,0.0,0.0],
        [1.0,0.0,0.0],
        [0.0,1.0,0.0],
        [0.0,1.0,0.0],
        [0.0,0.0,1.0],
        [0.0,0.0,1.0],
    ]
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_STRIP)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

    if borda:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor3f(0,0,0)
        glBegin(GL_TRIANGLE_STRIP)
        for v in vertices:
            glVertex2fv(v)
        glEnd()

# FunÃ§Ã£o que desenha um cÃ­rculo (ou polÃ­gono regular de N lados)
def circulo(borda=True):
    vertices = []                           # lista que conterÃ¡ as coordenadas dos vÃ©rtices
    cores = []                              # lista que conterÃ¡ as cores dos vÃ©rtices
    divisions = 36                          # quantidade de divisÃµes do cÃ­rculo (qtd de lados do polÃ­gono regular)
    radius = 0.5                            # raio do cÃ­rculo
    vertices.append([0,0])                  # inserindo o centro do cÃ­rculo na lista de vÃ©rtices
    cores.append([1.0,1.0,1.0])             # inserindo a cor do centro do cÃ­rculo na lista de cores
    for i in range(divisions+1):            # repetindo uma vez a mais para fechar o cÃ­rculo
        angle = i*360/divisions             # Ã¢ngulo central de cada vÃ©rtice
        x = radius * cos(radians(angle))    # coordenadas calculadas usando o ciclo trigonomÃ©trico (eixo x = cossenos)
        y = radius * sin(radians(angle))    # coordenadas calculadas usando o ciclo trigonomÃ©trico (eixo y = senos)
        vertices.append([x,y])              # inserindo novo vÃ©rtice na lista de vÃ©rtices
        cores.append([1.0,0.0,0.0])         # inserindo cor do novo vÃ©rtice na lista de cores
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_FAN)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

    if borda:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor3f(0,0,0)
        glBegin(GL_TRIANGLE_FAN)
        for v in vertices:
            glVertex2fv(v)
        glEnd()
    
# FunÃ§Ã£o usada para atualizar o desenho da tela
def render():
    glClear(GL_COLOR_BUFFER_BIT)    # atribui a cor definida em glClearColor a todos os pixels

    #pontos()
    segmentosDeReta()
    # linhaConectada()
    # triangulos()
    # triangulosConectados()
    # circulo()

# FunÃ§Ã£o principal
def main():
    glfw.init()                                                      # inicializa GLFW
    window = glfw.create_window(500,500,'02 - Primitivas',None,None) # criando a janela
    glfw.make_context_current(window)                                # atribuindo um contexto OpenGL a janela
    initialize()                                                     # funÃ§Ã£o com minhas configuraÃ§Ãµes iniciais
    while not glfw.window_should_close(window):                      # laÃ§o principal
        glfw.poll_events()                                           # tratamento de entrada
        render()                                                  # funÃ§Ã£o com atualizaÃ§Ã£o do desenho
        glfw.swap_buffers(window)                                    # troca frame buffer exibido na tela (double buffering)
    glfw.terminate()                                                 # finaliza GLFW

if __name__ == '__main__':
    main()