import pygame

pygame.init()

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Monkey Jumper: Demo")

azul = (0, 100, 255)
preto = (0, 0, 0)

clock = pygame.time.Clock()

rodando = True

x = 300
y = 500

velocidade = 300
velocidade_y = 0

vDash = 150
def banana(x,y):
    bnTO = pygame.image.load("bananaTO.png").convert_alpha()
    bn = pygame.transform.scale(bnTO, (64, 64))
    janela.blit(bn, (x,y))

gravidade = 1200
forca_pulo = -600
super_pulo = -850

chao = 500
pulando = False

while rodando:

    dt = clock.tick(60) / 1000

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                rodando = False

            if evento.key in (pygame.K_SPACE, pygame.K_w) and not pulando:

                teclas = pygame.key.get_pressed()

                if teclas[pygame.K_LSHIFT]:
                    velocidade_y = super_pulo
                else:
                    velocidade_y = forca_pulo

                pulando = True

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 3:

                teclas = pygame.key.get_pressed()

                if teclas[pygame.K_d]:
                    if teclas[pygame.K_w]:
                        x += vDash
                        y -= vDash
                    else:
                        x+= vDash

                elif teclas[pygame.K_a]:
                    if teclas[pygame.K_w]:
                        x -= vDash
                        y -= vDash
                    else:
                        x -= vDash

                elif teclas[pygame.K_w]:
                    y-= vDash

                elif teclas[pygame.K_s]:
                    y+= vDash

    teclas = pygame.key.get_pressed()

    velocidade = 600 if teclas[pygame.K_LSHIFT] else 300

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        x -= velocidade * dt

    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        x += velocidade * dt

    velocidade_y += gravidade * dt
    y += velocidade_y * dt

    if y >= chao:
        y = chao
        velocidade_y = 0
        pulando = False

    x = max(0, min(x, 750))

    janela.fill(azul)

    pygame.draw.rect(janela, preto, (int(x), int(y), 50, 50))
    banana(500,500)
    pygame.display.update()

pygame.quit()