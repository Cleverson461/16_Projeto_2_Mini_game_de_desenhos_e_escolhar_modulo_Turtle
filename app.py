from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

# Definir a velocidade
t.speed(1)

while True:
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás" ')
    if direcao == 'f':
        distancia = int(input('Quantos pixels devemos movimentar para a frente? '))
        movimentar_para_lado = input('Rotacionar para d:direita, e:esquerda n:não rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar? '))
            # Rotacionar em X graus para direita
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            # Rotacionar em X graus para esquerda
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(input('Quantos pixels devemos movimentar para a trás? '))
        movimentar_para_lado = input('Rotacionar para d:direita, e:esquerda n:não rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar? '))
            # Rotacionar em X graus para direita
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            # Rotacionar em X graus para esquerda
            t.left(angulo)
        t.forward(distancia)
    resposta = input('Continuar andando?')
    if resposta not in ('sim', 's'):
        break

""" # Movimentar a turtle para frente
t.forward(100)

t.right(90)
t.forward(100)

# Rotacionar em X graus para esquerda
t.left(90)
t.forward(100)

# Movimentar a turtle para trás
t.backward(200)
input() """