import glfw 
from OpenGL.GL import *
from PIL import Image

def inicializar():
    glClearColor(1, 1, 1, 1) 
    glLineWidth(5)
    glPointSize(20)

def render():
    glClear(GL_COLOR_BUFFER_BIT)

def pontosDistintos():

    vertices = [
    [-0.5, -0.5],   # vermelho
    [0.5, -0.5], # verde    
    [-0.5, 0.5], # roxo  
    [0.5, 0.5] # azul   
    ]

    cores = [
    [1.0, 0.0, 0.0],    # vermelho
    [0.0, 1.0, 0.0],   # verde
    [1.0, 0.0, 1.0],    # roxo
    [0.0, 0.0, 1.0]     # azul
    ]

    glBegin(GL_POINTS)
    for v, c in zip(vertices, cores):
        glColor3fv(c) # colore antes e faz o vertice?
        glVertex2fv(v)
    glEnd()


def linhasParalelas():
    vertices = [
    [-0.5, 0.0], # linha amarela (N)
    [0, 0.5], # linha amarela (P)
    [-0.5, -0.5], # linha azul (N)
    [0.5, 0.5], # linha azul (P)
    [0.0, -0.5], # linha roxa (N)
    [0.5, 0.0] # linha roxa (P)
    ]

    cores = [
        [1.0, 1.0, 0],
        [1.0, 1.0, 0],
        [0.0, 1.0, 1.0],
        [0.0, 1.0, 1.0],
        [1.0, 0.0, 1.0],
        [1.0, 0.0, 1.0]


    ]

    glBegin(GL_LINES)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

def m():
    vertices = [
        [-0.5, -0.5],
        [-0.5, 0.5],
        [0.0, -0.2],
        [0.5, 0.5],
        [0.5, -0.5]
    ]

    cores = [
        [1.0, 0.0, 0.0],
        [0.5, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [0.5, 0.0, 0.0],
        [1.0, 0.0, 0.0]
    ]

    glBegin(GL_LINE_STRIP)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

def estrela():
    
    vertices = [
        [-0.15, 0.15], #preto-amarelo
        [0.0, 0.7], #amarelo
        [0.0, 0.7], #amarelo
        [0.15, 0.15], #preto-amarelo
        [-0.15, 0.15], #preto
        [-0.5, 0.0], # vermelho
        [0.15, 0.15], #preto-amarelo direito
        [0.5, 0.0], # azul
        [-0.5, 0.0], # vermelho
        [-0.15, -0.15], # preto-vermelho (se ligando na esuqerda)
        [0.5, 0.0], # azul repetido 
        [0.15, -0.15], # preto?
        [0.0, -0.7], #verde
        [-0.15, -0.15], # preto
        [0.0, -0.7], #verde
        [0.15, -0.15] #preto

    ]

    cores = [
        [0.0, 0.0, 0.0],
        [1.0, 1.0, 0.0], #amarelo
        [1.0, 1.0, 0.0], #amarelo
        [0.0, 0.0, 0.0], #preto
        [0.0, 0.0, 0.0], #preto
        [1.0, 0.0, 0.0], #vermelho
        [0.0, 0.0, 0.0], # preto direito
        [0.0, 0.0, 1.0], # azul
        [1.0, 0.0, 0.0], # vermelho
        [0.0, 0.0, 0.0], #preto
        [0.0, 0.0, 1.0], # azul repetido
        [0.0, 0.0, 0.0], #preto
        [0.0, 1.0, 0.0], #verde
        [0.0, 0.0, 0.0], #preto-verde
        [0.0, 1.0, 0.0], #verde
        [0.0, 0.0, 0.0] #ultimo preto
        
    ]

    glBegin(GL_LINES)
    for v, c in zip(vertices, cores): #primeiro colore e depois coloca os pontos
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

def triangulos(borda = True): # fazer minha função de triangulos
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
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)       # novamente, preencha com a seguinte config
    glBegin(GL_TRIANGLES)                           # é um triangulo
    for v, c in zip(vertices, cores):
        glColor3fv(c)                               # coloque essas cores
        glVertex2fv(v)
    glEnd()

    if borda:                                       
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)   # nas faces, faça um triangulo de linhas
        glColor3f(0,0,0)                            # coloque a cor preta
        glBegin(GL_TRIANGLES)
        for v in vertices:
            glVertex2fv(v)
        glEnd()

def quadrados(borda = True):
    # colocar as posicoes mais proximas do eixo x
    vertices = [
    
    [0.4, 0.4], # roxo? Lilas, sla
    [0.7, 0.4], # roxo? Lilas, sla
    [0.7, 0.8], # roxo? Lilas, sla
    [0.4, 0.8], # roxo? Lilas, sla

    [-0.4, 0.4], # verde
    [-0.7, 0.4], # verde
    [-0.7, 0.8], # verde
    [-0.4, 0.8], # verde

    [-0.7, -0.4], # laranja
    [-0.4, -0.4], # laranja
    [-0.4, -0.8], # laranja
    [-0.7, -0.8], # laranja
    
    [0.4, -0.4],
    [0.7, -0.4],
    [0.7, -0.8],
    [0.4, -0.8]

    ]

    cores = [
        [0.9, 0.0, 0.5], # roxo? Lilas, sla
        [0.9, 0.0, 0.5], # roxo? Lilas, sla
        [0.9, 0.0, 0.5], # roxo? Lilas, sla
        [0.9, 0.0, 0.5], # roxo? Lilas, sla

        [0.0, 1.0, 0.0], # verde
        [0.0, 1.0, 0.0], # verde
        [0.0, 1.0, 0.0], # verde
        [0.0, 1.0, 0.0], # verde

        [1.0, 0.5, 0.0], # laranja
        [1.0, 0.5, 0.0], # laranja
        [1.0, 0.5, 0.0], # laraja
        [1.0, 0.5, 0.0], # laranja

        [0.0, 0.3, 0.9], # azul
        [0.0, 0.3, 0.9], # azul
        [0.0, 0.3, 0.9], # azul
        [0.0, 0.3, 0.9] # azul
    ]
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) # blz, preencha meus quadrados com as cores da lista
    glBegin(GL_QUADS) # faça essa forma
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

    if borda:                                       
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) # nas faces, coloque essas linhas
        glColor3f(0,0,0)                            
        glBegin(GL_QUADS) # as linha sseguiração esse formato
        for v in vertices:
            glVertex2fv(v)
        glEnd()



def trianguloComBorda():
    vertices = [
        [-0.5, -0.5],
        [0.5, -0.5],
        [0.0, 0.6]
    ]

    cores = [
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0]
    ]

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLES)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

   
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.0) # as cores dos vertices a serem desenhados
    for v in vertices:
        glVertex2fv(v)
    glEnd()

def fortaleza():
    # triangulo
    verticesDoRetangulo = [ # melhoras as coordenadas, ta muito pra baixo
        [-0.6, 0.5],
        [-0.6, 0.2],
        [0.6, 0.2],
        [0.6, 0.5]
    ]

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    for vertices in verticesDoRetangulo:
        glVertex2fv(vertices)
    glEnd()

    verticesDoTrianguloAzul = [
        [-0.6, 0.1],
        [-0.1, 0.1],
        [-0.1, -0.8]
    ]

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)
    for vertices in verticesDoTrianguloAzul:
        glVertex2fv(vertices)
    glEnd()

    verticesDoTrianguloVermelho = [
        [0.6, 0.1],
        [0.1, 0.1],
        [0.1, -0.8]
    ]
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    for vertices in verticesDoTrianguloVermelho:
        glVertex2fv(vertices)
    glEnd()

def octogono():
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

    verticesDoTrianguloAcima = [
        [-0.5, 0.5],
        [0.0, 0.7], # do meio
        [0.5, 0.5]
    ]
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.498, 0.996)
    for v in verticesDoTrianguloAcima:
        glVertex2fv(v)
    glEnd()

    verticesDoTrianguloAbaixo = [
        [-0.5, -0.5],
        [0.0, -0.7], # do meio
        [0.5, -0.5]
    ]
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.498, 0.996)
    for v in verticesDoTrianguloAbaixo:
        glVertex2fv(v)
    glEnd()

    verticesDoTrianguloDaEsquerda = [
        [-0.5, 0.5],
        [-0.63, 0.0], # do meio
        [-0.5, -0.5]
    ]
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.498, 0.996)
    for v in verticesDoTrianguloDaEsquerda:
        glVertex2fv(v)
    glEnd()

    verticesDoTrianguloDaDireita = [
        [0.5, 0.5],
        [0.63, 0.0], # do meio
        [0.5, -0.5]
    ]
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.498, 0.996)
    for v in verticesDoTrianguloDaDireita:
        glVertex2fv(v)
    glEnd()

    verticesDasBorda = [
        # fazer isso aki
    ]

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
        #pontosDistintos()
        #linhasParalelas()
        #m()
        #estrela()
        #triangulos()
        #quadrados()
        #trianguloComBorda()
        #fortaleza()
        octogono()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == '__main__':
    main()
