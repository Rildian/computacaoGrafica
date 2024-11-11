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
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) 
    glBegin(GL_QUADS)
    for v, c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)
    glEnd()

    if borda:                                       # caso deseje visualizar as bordas dos polÃ­gonos na cor preta
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)   # habilitando a rasterizaÃ§Ã£o apenas das arestas dos polÃ­gonos
        glColor3f(0,0,0)                            # atribuindo uma cor uniforme para todos os vÃ©rtices
        glBegin(GL_QUADS)
        for v in vertices:
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
        #pontosDistintos()
        #linhasParalelas()
        #m()
        #estrela()
        #triangulos()
        quadrados()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == '__main__':
    main()
