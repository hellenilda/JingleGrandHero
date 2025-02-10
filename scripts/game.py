import pygame, random, sys, pyautogui, os
from button import Button
import threading as th
from tkinter import messagebox
import socket
import threading as th

usuario = os.getlogin()

def Hosth():
    messagebox.showinfo("Saudações",f"Seja muito bem vindo ao mundo Jingle Grand Hero caro {usuario}")

def main():
    pygame.init()
    mhundo = "C:\\Users\\Hellenilda\\Documents\\Algoritmos\\Python\\Jingle Grand Hero 24-11\\Mundos\\"
    sprite = "C:\\Users\\Hellenilda\\Documents\\Algoritmos\\Python\\Jingle Grand Hero 24-11\\sprites\\"
    sons = "C:\\Users\\Hellenilda\\Documents\\Algoritmos\\Python\\Jingle Grand Hero 24-11\\sons\\"
    pontuacaoAT = "C:\\Users\\Hellenilda\\Documents\\Algoritmos\\Python\\Jingle Grand Hero 24-11\\resultado\\"

    tela = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Jingle Grand Hero")

    largura = 1280
    altura = 720

    backgroundMenu = pygame.image.load(f"{sprite}Funddy.png")
    musicaInicio = pygame.mixer.Sound(f"{sons}musicaInicio.wav")
    somBotao = pygame.mixer.Sound(f"{sons}somBotao.wav")
    somMoeda = pygame.mixer.Sound(f"{sons}somMoeda.wav")
    somColisao = pygame.mixer.Sound(f"{sons}somColisao.wav")
    trilhaSonora1 = pygame.mixer.Sound(f"{sons}trilhaSonora1.mp3")
    trilhaSonora2 = pygame.mixer.Sound(f"{sons}trilhaSonora2.mp3")
    trilhaSonora3 = pygame.mixer.Sound(f"{sons}trilhaSonora3.mp3")

    placa = pygame.image.load(f'{sprite}Placa_invertida.png')
    placa = pygame.transform.scale(placa, ( 260 , 200 ))

    pontoX = pygame.image.load(f"{sprite}ponto_inicial.png").convert_alpha()
    pontoX1 = pygame.image.load(f"{sprite}placar_2.0.png")
    carr = pygame.image.load(f"{sprite}carregamento.png")

    def sond_off():
            pygame.mixer.Sound.set_volume( musicaInicio , 0 )
            pygame.mixer.Sound.set_volume( somBotao , 0 )
            pygame.mixer.Sound.set_volume( somColisao , 0 )
            pygame.mixer.Sound.set_volume( somMoeda , 0 )
            pygame.mixer.Sound.set_volume( trilhaSonora1 , 0 )
            pygame.mixer.Sound.set_volume( trilhaSonora2 , 0 )
            pygame.mixer.Sound.set_volume( trilhaSonora3 , 0 )
    def sond_on():
            pygame.mixer.Sound.set_volume( musicaInicio , 1 )
            pygame.mixer.Sound.set_volume( somBotao , 1 )
            pygame.mixer.Sound.set_volume( somColisao , 1 )
            pygame.mixer.Sound.set_volume( somMoeda , 1 )
            pygame.mixer.Sound.set_volume( trilhaSonora1 , 1 )
            pygame.mixer.Sound.set_volume( trilhaSonora2 , 1 )
            pygame.mixer.Sound.set_volume( trilhaSonora3 , 1 )

    def gerarFonte(tamanho):
        return pygame.font.Font(f"{sprite}font.ttf", tamanho)

    def Mundo_facil():
        def Mundo_01f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 15
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora3)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Nave.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_verde.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_03.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_azul(): #Final do placar fica na posição X = 600
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_azul():
                    if placar > 0:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_azul()
            while gameloop:

                placa_azul()
                clock.tick(30)# 30

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')

                ######################################## COLISÃO ########################################
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pyautogui.sleep(1)

                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)


                                # envio dos pontos
                                ###################################################################################
                                # localIP     = "192.168.0.100"
                                # userr = os.getlogin()
                                # with open('C:\\Users\\Robótica-LaISER\\Desktop\Jingle Grand Hero  23-11-22\\resultado\\pontuacaoAtual.txt', 'w') as aqu:
                                #     aqu.write(userr)
                                #     with open('C:\\Users\\Robótica-LaISER\\Desktop\Jingle Grand Hero  23-11-22\\resultado\\pontuacaoAtual.txt', 'r') as dd:
                                #         asz = dd.read()
                                #         print(asz)

                                # msg = ( f"{userr} | {d}")
                                # print("esta é nossa mensagem : ", msg)
                                # bytesToSend         = str.encode(msg)
                                # serverAddressPort   = (localIP, 2001)
                                # bufferSize          = 1024
                                # UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                                # UDPClientSocket.sendto(bytesToSend, serverAddressPort)
                                # UDPClientSocket.recvfrom(bufferSize)


                                ###################################################################################

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_01f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()

                #############################################################################################
                if placar == 15:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")

                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)


                        #########################################################      Ganhando       #########################################################
                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)




                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_01f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()
                update()
                draw()

                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()
        def Mundo_02f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 15
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora3)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground2.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}v3.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_vermelho.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_02.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_azul(): #Final do placar fica na posição X = 600
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_azul():
                    if placar > 0:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_azul()

            while gameloop:
                placa_azul()
                clock.tick(30)# 30

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')

                ######################################## COLISÃO ########################################
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)

                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_02f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()

                #############################################################################################
                if placar == 15:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))

                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_02f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()
                update()
                draw()


                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()
        def Mundo_03f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 15
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora3)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}asfalto.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Pneu.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [170, 120])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_azul.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_04.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_azul(): #Final do placar fica na posição X = 600
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_azul():
                    if placar > 0:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_azul()

            while gameloop:
                placa_azul()
                clock.tick(30)# 30

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')

                ######################################## COLISÃO ########################################
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)

                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_03f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()

                #############################################################################################
                if placar == 15:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_03f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()
                update()
                draw()


                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()
        def Mundo_04f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 15
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora3)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground2.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Dragão.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_roxo.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_05.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_azul(): #Final do placar fica na posição X = 600
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_azul():
                    if placar > 0:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((131,11,255)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_azul()

            while gameloop:
                placa_azul()
                clock.tick(30)# 30

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')

                ######################################## COLISÃO ########################################
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)
                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_04f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()

                #############################################################################################
                if placar == 15:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    Mundo_04f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora3)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_facil()

                        pygame.display.update()
                update()
                draw()


                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()

        while True:
                    botaoOPCOES = pygame.mouse.get_pos()
                    tela.fill("white")
                    textoOPCOES = gerarFonte(35).render("Selecione o Mundo", True, "Black")
                    retanguloOPCOES = textoOPCOES.get_rect(center=(670, 80))
                    tela.blit(textoOPCOES, retanguloOPCOES)

                    M1 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_1.png"), pos=(280, 254),
                                        input_texto="", fonte=gerarFonte(00), corBase="white", corSobreposicao="white")
                    M1.changeColor(botaoOPCOES)
                    M1.update(tela)
                    M2 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_2.png"), pos=(935, 254),
                                        input_texto="", fonte=gerarFonte(0), corBase="white", corSobreposicao="white")
                    M2.changeColor(botaoOPCOES)
                    M2.update(tela)
                    M3 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_3.png"), pos=(309, 560),
                                        input_texto="", fonte=gerarFonte(0), corBase="#00BFFF", corSobreposicao="#32CD32")
                    M3.changeColor(botaoOPCOES)
                    M3.update(tela)
                    M4 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_4.png"), pos=(950, 537),
                                        input_texto="", fonte=gerarFonte(0), corBase="#00BFFF", corSobreposicao="#FF8C00")
                    M4.changeColor(botaoOPCOES)
                    M4.update(tela)


                    voltarr = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(70, 27),
                                    input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                    voltarr.changeColor(botaoOPCOES)
                    voltarr.update(tela)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if M1.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_01f()
                            if M2.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_02f()
                            if M3.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_03f()
                            if M4.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_04f()
                            if voltarr.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                nivel()
                    pygame.display.update()

    def Mundo_medio():
        def Mundo_01f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 10
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora1)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0
                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)
                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)
            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Nave.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_verde.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_03.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_vermelha(): #60 diamantes
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_vermelha():
                    if placar > 0:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 10, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 20, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 50, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 60, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 90, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 100, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 110, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 130, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 140, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 150, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 170, 30), border_radius=25)
                    if placar > 18:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 180, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 190, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 210, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 220, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 24:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 250, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 270, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 300, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 310, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 330, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 340, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 370, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 390, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 410, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 420, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 460, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 500, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 540, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_vermelha()

            while gameloop:
                placa_vermelha()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))
                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)


                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_01f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()

                if placar == 60:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_01f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()
                update()
                draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()
        def Mundo_02f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 10
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora1)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0
                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)
                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)
            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground2.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}v3.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_vermelho.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_02.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_vermelha(): #60 diamantes
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_vermelha():
                    if placar > 0:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 10, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 20, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 50, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 60, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 90, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 100, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 110, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 130, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 140, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 150, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 170, 30), border_radius=25)
                    if placar > 18:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 180, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 190, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 210, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 220, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 24:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 250, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 270, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 300, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 310, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 330, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 340, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 370, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 390, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 410, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 420, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 460, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 500, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 540, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_vermelha()

            while gameloop:
                placa_vermelha()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)


                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)


                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_02f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()

                if placar == 60:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_02f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()
                update()
                draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()
        def Mundo_03f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 10
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora1)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0
                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)
                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)
            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}asfalto.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Pneu.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [170, 120])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_azul.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_04.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_vermelha(): #60 diamantes
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_vermelha():
                    if placar > 0:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 10, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 20, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 50, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 60, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 90, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 100, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 110, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 130, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 140, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 150, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 170, 30), border_radius=25)
                    if placar > 18:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 180, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 190, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 210, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 220, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 24:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 250, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 270, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 300, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 310, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 330, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 340, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 370, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 390, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 410, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 420, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 460, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 500, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 540, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_vermelha()

            while gameloop:
                placa_vermelha()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)



                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_03f
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()

                if placar == 60:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_03f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()
                update()
                draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()
        def Mundo_04f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 10
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora1)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0
                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)
                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)
            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground2.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Dragão.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')
            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_roxo.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize
                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')
            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador
            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin
            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])
            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')
            BACKGROUND = pygame.image.load(f'{sprite}background_05.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])
            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)
            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)
            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)
            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)
            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_vermelha(): #60 diamantes
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_vermelha():
                    if placar > 0:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 10, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 20, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 40, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 50, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 60, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 80, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 90, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 100, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 110, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 120, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 130, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 140, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 150, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 160, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 170, 30), border_radius=25)
                    if placar > 18:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 180, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 190, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 210, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 220, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 24:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 240, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 250, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 270, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 280, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 300, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 310, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 330, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 340, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 360, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 370, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 390, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 410, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 420, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 440, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 460, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 480, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 500, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 520, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 540, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 560, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((178,34,34)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_vermelha()

            while gameloop:
                placa_vermelha()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)
                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0
                    print('Velocidade em 0')
                else:
                    velocidade = 12
                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)
                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.02
                    print('velocidade ALTERADA')
                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)



                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_04f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()

                if placar == 60:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    Mundo_04f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora1)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_medio()

                        pygame.display.update()
                update()
                draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botaoVoltarPLAY.checkForInput(botaoPLAY):
                            menuPrincipal()
                pygame.display.update()

        while True:
                    botaoOPCOES = pygame.mouse.get_pos()
                    tela.fill("white")
                    textoOPCOES = gerarFonte(35).render("Selecione o Mundo", True, "Black")
                    retanguloOPCOES = textoOPCOES.get_rect(center=(670, 80))
                    tela.blit(textoOPCOES, retanguloOPCOES)

                    M1 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_1.png"), pos=(280, 254),
                                        input_texto="", fonte=gerarFonte(00), corBase="white", corSobreposicao="white")
                    M1.changeColor(botaoOPCOES)
                    M1.update(tela)
                    M2 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_2.png"), pos=(935, 254),
                                        input_texto="", fonte=gerarFonte(0), corBase="white", corSobreposicao="white")
                    M2.changeColor(botaoOPCOES)
                    M2.update(tela)
                    M3 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_3.png"), pos=(309, 560),
                                        input_texto="", fonte=gerarFonte(0), corBase="#00BFFF", corSobreposicao="#32CD32")
                    M3.changeColor(botaoOPCOES)
                    M3.update(tela)
                    M4 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_4.png"), pos=(950, 537),
                                        input_texto="", fonte=gerarFonte(0), corBase="#00BFFF", corSobreposicao="#FF8C00")
                    M4.changeColor(botaoOPCOES)
                    M4.update(tela)


                    voltarr = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(70, 27),
                                    input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                    voltarr.changeColor(botaoOPCOES)
                    voltarr.update(tela)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if M1.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_01f()
                            if M2.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_02f()
                            if M3.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_03f()
                            if M4.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_04f()
                            if voltarr.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                nivel()
                    pygame.display.update()

    def Mundo_dificil():
        def Mundo_01f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 17
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora2)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo

            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Nave.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')

            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_verde.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')

            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador

            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin

            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])

            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')

            BACKGROUND = pygame.image.load(f'{sprite}background_03.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])

            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)

            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)

            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)

            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)

            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_verde():
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_verde():
                    if placar > 0:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 6, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 12, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 18, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 24, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 36, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 42, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 48, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 54, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 76, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 82, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 88, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 95, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 101, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 107, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 113, 30), border_radius=25)
                    if placar >= 18:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 119, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 125, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 131, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 137, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 143, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 149, 30), border_radius=25)
                    if placar > 24:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 155, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 161, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 167, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 173, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 176, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 182, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 188, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 194, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 206, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 212, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 218, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 224, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 236, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 242, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 248, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 254, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 266, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 272, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 278, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 284, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 296, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 302, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 308, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 314, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 326, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 332, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 338, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 344, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 356, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 362, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 368, 30), border_radius=25)
                    if placar >= 61:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 374, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 386, 30), border_radius=25)
                    if placar >= 63:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 394, 30), border_radius=25)
                    if placar >= 64:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 65:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 406, 30), border_radius=25)
                    if placar >= 66:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 412, 30), border_radius=25)
                    if placar >= 67:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 418, 30), border_radius=25)
                    if placar >= 68:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 424, 30), border_radius=25)
                    if placar > 69:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 70:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 436, 30), border_radius=25)
                    if placar >= 71:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 444, 30), border_radius=25)
                    if placar >= 72:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 73:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 456, 30), border_radius=25)
                    if placar >= 74:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 464, 30), border_radius=25)
                    if placar >= 75:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 76:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 476, 30), border_radius=25)
                    if placar >= 77:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 484, 30), border_radius=25)
                    if placar >= 78:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 79:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 496, 30), border_radius=25)
                    if placar >= 80:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 504, 30), border_radius=25)
                    if placar >= 81:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 82:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 516, 30), border_radius=25)
                    if placar >= 83:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 524, 30), border_radius=25)
                    if placar >= 84:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 85:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 536, 30), border_radius=25)
                    if placar >= 86:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 544, 30), border_radius=25)
                    if placar >= 87:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 88:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 556, 30), border_radius=25)
                    if placar >= 89:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 564, 30), border_radius=25)
                    if placar >= 90:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 572, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 574, 30), border_radius=25)
                    if placar >= 92:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 576, 30), border_radius=25)
                    if placar >= 93:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 578, 30), border_radius=25)
                    if placar >= 94:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 95:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 586, 30), border_radius=25)
                    if placar >= 96:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 588, 30), border_radius=25)
                    if placar >= 97:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 98:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 596, 30), border_radius=25)
                    if placar >= 99:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 598, 30), border_radius=25)
                    if placar >= 100:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_verde()

            def placars():
                if placar <= 25:
                    placa_verde()
                if placar >= 25:
                        placa_verde()
                if placar >= 50:
                    placa_verde()
            while gameloop:
                placars()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)

                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)

                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0 # bloqueio do chaooo
                    print('Velocidade em 0')
                else:
                    velocidade = 12

                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)


                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.20
                    print('velocidade ALTERADA')

                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora2 )
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)
                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_01f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()

                        pygame.display.update()
                if placar == 100:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_01f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()
                        pygame.display.update()
                update()
                draw()
                pygame.display.update()
        def Mundo_02f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 17
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora2)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground2.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo

            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}v3.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')

            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_vermelho.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')

            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador

            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin

            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])

            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')

            BACKGROUND = pygame.image.load(f'{sprite}background_02.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])

            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)

            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)

            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)

            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)

            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_verde():
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_verde():
                    if placar > 0:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 6, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 12, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 18, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 24, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 36, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 42, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 48, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 54, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 76, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 82, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 88, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 95, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 101, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 107, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 113, 30), border_radius=25)
                    if placar >= 18:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 119, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 125, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 131, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 137, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 143, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 149, 30), border_radius=25)
                    if placar > 24:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 155, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 161, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 167, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 173, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 176, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 182, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 188, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 194, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 206, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 212, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 218, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 224, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 236, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 242, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 248, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 254, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 266, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 272, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 278, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 284, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 296, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 302, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 308, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 314, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 326, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 332, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 338, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 344, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 356, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 362, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 368, 30), border_radius=25)
                    if placar >= 61:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 374, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 386, 30), border_radius=25)
                    if placar >= 63:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 394, 30), border_radius=25)
                    if placar >= 64:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 65:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 406, 30), border_radius=25)
                    if placar >= 66:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 412, 30), border_radius=25)
                    if placar >= 67:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 418, 30), border_radius=25)
                    if placar >= 68:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 424, 30), border_radius=25)
                    if placar > 69:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 70:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 436, 30), border_radius=25)
                    if placar >= 71:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 444, 30), border_radius=25)
                    if placar >= 72:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 73:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 456, 30), border_radius=25)
                    if placar >= 74:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 464, 30), border_radius=25)
                    if placar >= 75:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 76:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 476, 30), border_radius=25)
                    if placar >= 77:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 484, 30), border_radius=25)
                    if placar >= 78:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 79:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 496, 30), border_radius=25)
                    if placar >= 80:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 504, 30), border_radius=25)
                    if placar >= 81:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 82:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 516, 30), border_radius=25)
                    if placar >= 83:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 524, 30), border_radius=25)
                    if placar >= 84:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 85:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 536, 30), border_radius=25)
                    if placar >= 86:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 544, 30), border_radius=25)
                    if placar >= 87:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 88:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 556, 30), border_radius=25)
                    if placar >= 89:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 564, 30), border_radius=25)
                    if placar >= 90:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 572, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 574, 30), border_radius=25)
                    if placar >= 92:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 576, 30), border_radius=25)
                    if placar >= 93:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 578, 30), border_radius=25)
                    if placar >= 94:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 95:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 586, 30), border_radius=25)
                    if placar >= 96:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 588, 30), border_radius=25)
                    if placar >= 97:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 98:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 596, 30), border_radius=25)
                    if placar >= 99:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 598, 30), border_radius=25)
                    if placar >= 100:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_verde()

            def placars():
                if placar <= 25:
                    placa_verde()
                if placar >= 25:
                        placa_verde()
                if placar >= 50:
                    placa_verde()
            while gameloop:
                placars()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)

                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)

                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0 # bloqueio do chaooo
                    print('Velocidade em 0')
                else:
                    velocidade = 12

                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)


                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.20
                    print('velocidade ALTERADA')

                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora2 )
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)
                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_02f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()

                        pygame.display.update()
                if placar == 100:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_02f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()
                        pygame.display.update()
                update()
                draw()
                pygame.display.update()
        def Mundo_03f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 17
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora2)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}asfalto.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo

            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Pneu.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')

            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_azul.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')

            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador

            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin

            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])

            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')

            BACKGROUND = pygame.image.load(f'{sprite}background_04.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])

            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)

            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)

            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)

            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)

            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_verde():
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_verde():
                    if placar > 0:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 6, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 12, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 18, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 24, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 36, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 42, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 48, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 54, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 76, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 82, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 88, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 95, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 101, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 107, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 113, 30), border_radius=25)
                    if placar >= 18:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 119, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 125, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 131, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 137, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 143, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 149, 30), border_radius=25)
                    if placar > 24:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 155, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 161, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 167, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 173, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 176, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 182, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 188, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 194, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 206, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 212, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 218, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 224, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 236, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 242, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 248, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 254, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 266, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 272, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 278, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 284, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 296, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 302, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 308, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 314, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 326, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 332, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 338, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 344, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 356, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 362, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 368, 30), border_radius=25)
                    if placar >= 61:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 374, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 386, 30), border_radius=25)
                    if placar >= 63:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 394, 30), border_radius=25)
                    if placar >= 64:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 65:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 406, 30), border_radius=25)
                    if placar >= 66:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 412, 30), border_radius=25)
                    if placar >= 67:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 418, 30), border_radius=25)
                    if placar >= 68:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 424, 30), border_radius=25)
                    if placar > 69:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 70:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 436, 30), border_radius=25)
                    if placar >= 71:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 444, 30), border_radius=25)
                    if placar >= 72:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 73:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 456, 30), border_radius=25)
                    if placar >= 74:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 464, 30), border_radius=25)
                    if placar >= 75:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 76:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 476, 30), border_radius=25)
                    if placar >= 77:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 484, 30), border_radius=25)
                    if placar >= 78:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 79:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 496, 30), border_radius=25)
                    if placar >= 80:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 504, 30), border_radius=25)
                    if placar >= 81:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 82:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 516, 30), border_radius=25)
                    if placar >= 83:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 524, 30), border_radius=25)
                    if placar >= 84:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 85:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 536, 30), border_radius=25)
                    if placar >= 86:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 544, 30), border_radius=25)
                    if placar >= 87:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 88:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 556, 30), border_radius=25)
                    if placar >= 89:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 564, 30), border_radius=25)
                    if placar >= 90:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 572, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 574, 30), border_radius=25)
                    if placar >= 92:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 576, 30), border_radius=25)
                    if placar >= 93:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 578, 30), border_radius=25)
                    if placar >= 94:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 95:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 586, 30), border_radius=25)
                    if placar >= 96:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 588, 30), border_radius=25)
                    if placar >= 97:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 98:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 596, 30), border_radius=25)
                    if placar >= 99:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 598, 30), border_radius=25)
                    if placar >= 100:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_verde()

            def placars():
                if placar <= 25:
                    placa_verde()
                if placar >= 25:
                        placa_verde()
                if placar >= 50:
                    placa_verde()
            while gameloop:
                placars()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)

                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)

                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0 # bloqueio do chaooo
                    print('Velocidade em 0')
                else:
                    velocidade = 12

                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)


                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.20
                    print('velocidade ALTERADA')

                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora2 )
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)
                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_03f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()

                        pygame.display.update()
                if placar == 100:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_03f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()
                        pygame.display.update()
                update()
                draw()
                pygame.display.update()
        def Mundo_04f():
            botaoPLAY = pygame.mouse.get_pos()
            velocidade = 10
            velocidadeJogo = 17
            larguraCHAO = 2 * largura
            alturaCHAO = 30
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(trilhaSonora2)
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image_run = [pygame.image.load(f'{sprite}000.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}001.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}002.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}006.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}005.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}004.png').convert_alpha(),
                                    pygame.image.load(f'{sprite}003.png').convert_alpha(),
                                    ]
                    self.frameQueda = pygame.image.load(f'{sprite}007.png').convert_alpha()
                    self.image = pygame.image.load(f'{sprite}000.png').convert_alpha()
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imagemAtual = 0


                def update(self, *args):
                    def moverPersonagem(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_d]:
                            self.rect[0] += velocidadeJogo
                        if key[pygame.K_a]:
                            self.rect[0] -= velocidadeJogo
                        self.imagemAtual = (self.imagemAtual + 1) % 10
                        self.image = self.image_run[self.imagemAtual]
                        self.image = pygame.transform.scale(self.image,[100, 100])
                    moverPersonagem(self)
                    self.rect[1] += velocidade
                    def fly(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                            self.rect[1] -= 29
                            self.image = pygame.transform.scale(self.frameQueda, [100, 100])
                    fly(self)

                    def fall(self):
                        key = pygame.key.get_pressed()
                        if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                            self.image = self.frameQueda
                            self.image = pygame.transform.scale(self.image, [100, 100])
                    fall(self)


            class Ground(pygame.sprite.Sprite):
                def __init__(self, xpos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ground2.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image,(larguraCHAO, alturaCHAO))
                    self.rect = self.image.get_rect()
                    self.rect[0] = xpos
                    self.rect[1] = altura - alturaCHAO

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo

            class Obstacles(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}Dragão.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [100, 100])
                    self.rect = pygame.Rect(100, 100, 100, 100)
                    self.rect[0] = xpos
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('obstacle')

            class rubi(pygame.sprite.Sprite):
                def __init__(self, xpos, ysize):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(f'{sprite}ruby_roxo.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [40, 40])
                    self.rect = pygame.Rect(100, 100, 20, 20)
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect[0] = xpos
                    self.rect[1] = altura - ysize

                def update(self, *args):
                    self.rect[0] -= velocidadeJogo
                    print('coin')

            def posicaoAleatoriaObstaculos(xpos):
                largura = random.randint(120, 600)
                coelhoVoador = Obstacles(xpos, largura)
                return coelhoVoador

            def posicaoAleatoriaRubi(xpos):
                largura = random.randint(60, 500)
                coin = rubi(xpos, largura)
                return coin

            def fora_da_tela(sprite):
                return sprite.rect[0] < -(sprite.rect[2])

            pygame.init()
            telaDeJogo = pygame.display.set_mode([largura, altura])
            pygame.display.set_caption('Jingle Grand Hero')

            BACKGROUND = pygame.image.load(f'{sprite}background_05.png')
            BACKGROUND = pygame.transform.scale(BACKGROUND,[largura, altura])

            playerGroup = pygame.sprite.Group()
            player = Player()
            playerGroup.add(player)

            groundGroup = pygame.sprite.Group()
            for i in range(2):
                ground = Ground(largura * i)
                groundGroup.add(ground)

            grupoRubi = pygame.sprite.Group()
            for i in range(2):
                coin = posicaoAleatoriaRubi(largura * i + 1000)
                grupoRubi.add(coin)

            obstacleGroup = pygame.sprite.Group()
            for i in range(2):
                obstacle = posicaoAleatoriaObstaculos(largura * i + 1000)
                obstacleGroup.add(obstacle)

            gameloop = True
            def draw():
                playerGroup.draw(telaDeJogo)
                groundGroup.draw(telaDeJogo)
                obstacleGroup.draw(telaDeJogo)
                grupoRubi.draw(telaDeJogo)
            def update():
                groundGroup.update()
                playerGroup.update()
                obstacleGroup.update()
                grupoRubi.update()
            clock = pygame.time.Clock()

            placar = 0

            def placa_verde():
                telaDeJogo.blit(BACKGROUND, (0, 0))
                tela.blit(pontoX1, (0,0))

                def barraDeProgresso_verde():
                    if placar > 0:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 6, 30), border_radius=25)
                    if placar >= 2:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 12, 30), border_radius=25)
                    if placar >= 3:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 18, 30), border_radius=25)
                    if placar >= 4:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 24, 30), border_radius=25)
                    if placar >= 5:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 30, 30), border_radius=25)
                    if placar >= 6:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 36, 30), border_radius=25)
                    if placar >= 7:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 42, 30), border_radius=25)
                    if placar >= 8:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 48, 30), border_radius=25)
                    if placar >= 9:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 54, 30), border_radius=25)
                    if placar >= 10:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 70, 30), border_radius=25)
                    if placar >= 11:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 76, 30), border_radius=25)
                    if placar >= 12:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 82, 30), border_radius=25)
                    if placar >= 13:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 88, 30), border_radius=25)
                    if placar >= 14:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 95, 30), border_radius=25)
                    if placar >= 15:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 101, 30), border_radius=25)
                    if placar >= 16:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 107, 30), border_radius=25)
                    if placar >= 17:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 113, 30), border_radius=25)
                    if placar >= 18:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 119, 30), border_radius=25)
                    if placar >= 19:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 125, 30), border_radius=25)
                    if placar >= 20:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 131, 30), border_radius=25)
                    if placar >= 21:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 137, 30), border_radius=25)
                    if placar >= 22:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 143, 30), border_radius=25)
                    if placar >= 23:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 149, 30), border_radius=25)
                    if placar > 24:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 155, 30), border_radius=25)
                    if placar >= 25:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 161, 30), border_radius=25)
                    if placar >= 26:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 167, 30), border_radius=25)
                    if placar >= 27:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 173, 30), border_radius=25)
                    if placar >= 28:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 176, 30), border_radius=25)
                    if placar >= 29:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 182, 30), border_radius=25)
                    if placar >= 30:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 188, 30), border_radius=25)
                    if placar >= 31:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 194, 30), border_radius=25)
                    if placar >= 32:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 200, 30), border_radius=25)
                    if placar >= 33:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 206, 30), border_radius=25)
                    if placar >= 34:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 212, 30), border_radius=25)
                    if placar >= 35:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 218, 30), border_radius=25)
                    if placar >= 36:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 224, 30), border_radius=25)
                    if placar >= 37:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 230, 30), border_radius=25)
                    if placar >= 38:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 236, 30), border_radius=25)
                    if placar >= 39:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 242, 30), border_radius=25)
                    if placar >= 40:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 248, 30), border_radius=25)
                    if placar >= 41:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 254, 30), border_radius=25)
                    if placar >= 42:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 260, 30), border_radius=25)
                    if placar >= 43:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 266, 30), border_radius=25)
                    if placar >= 44:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 272, 30), border_radius=25)
                    if placar >= 45:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 278, 30), border_radius=25)
                    if placar >= 46:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 284, 30), border_radius=25)
                    if placar >= 47:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 290, 30), border_radius=25)
                    if placar >= 48:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 296, 30), border_radius=25)
                    if placar >= 49:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 302, 30), border_radius=25)
                    if placar >= 50:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 308, 30), border_radius=25)
                    if placar >= 51:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 314, 30), border_radius=25)
                    if placar >= 52:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 320, 30), border_radius=25)
                    if placar >= 53:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 326, 30), border_radius=25)
                    if placar >= 54:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 332, 30), border_radius=25)
                    if placar >= 55:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 338, 30), border_radius=25)
                    if placar >= 56:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 344, 30), border_radius=25)
                    if placar >= 57:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 350, 30), border_radius=25)
                    if placar >= 58:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 356, 30), border_radius=25)
                    if placar >= 59:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 362, 30), border_radius=25)
                    if placar >= 60:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 368, 30), border_radius=25)
                    if placar >= 61:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 374, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 380, 30), border_radius=25)
                    if placar >= 62:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 386, 30), border_radius=25)
                    if placar >= 63:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 394, 30), border_radius=25)
                    if placar >= 64:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 400, 30), border_radius=25)
                    if placar >= 65:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 406, 30), border_radius=25)
                    if placar >= 66:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 412, 30), border_radius=25)
                    if placar >= 67:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 418, 30), border_radius=25)
                    if placar >= 68:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 424, 30), border_radius=25)
                    if placar > 69:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 430, 30), border_radius=25)
                    if placar >= 70:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 436, 30), border_radius=25)
                    if placar >= 71:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 444, 30), border_radius=25)
                    if placar >= 72:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 450, 30), border_radius=25)
                    if placar >= 73:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 456, 30), border_radius=25)
                    if placar >= 74:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 464, 30), border_radius=25)
                    if placar >= 75:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 470, 30), border_radius=25)
                    if placar >= 76:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 476, 30), border_radius=25)
                    if placar >= 77:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 484, 30), border_radius=25)
                    if placar >= 78:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 490, 30), border_radius=25)
                    if placar >= 79:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 496, 30), border_radius=25)
                    if placar >= 80:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 504, 30), border_radius=25)
                    if placar >= 81:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 510, 30), border_radius=25)
                    if placar >= 82:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 516, 30), border_radius=25)
                    if placar >= 83:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 524, 30), border_radius=25)
                    if placar >= 84:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 530, 30), border_radius=25)
                    if placar >= 85:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 536, 30), border_radius=25)
                    if placar >= 86:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 544, 30), border_radius=25)
                    if placar >= 87:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 550, 30), border_radius=25)
                    if placar >= 88:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 556, 30), border_radius=25)
                    if placar >= 89:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 564, 30), border_radius=25)
                    if placar >= 90:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 570, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 572, 30), border_radius=25)
                    if placar >= 91:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 574, 30), border_radius=25)
                    if placar >= 92:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 576, 30), border_radius=25)
                    if placar >= 93:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 578, 30), border_radius=25)
                    if placar >= 94:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 580, 30), border_radius=25)
                    if placar >= 95:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 586, 30), border_radius=25)
                    if placar >= 96:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 588, 30), border_radius=25)
                    if placar >= 97:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 590, 30), border_radius=25)
                    if placar >= 98:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 596, 30), border_radius=25)
                    if placar >= 99:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 598, 30), border_radius=25)
                    if placar >= 100:
                        pygame.draw.rect(tela, ((60,179,113)), (323, 30, i + 600, 30), border_radius=25)

                barraDeProgresso_verde()

            def placars():
                if placar <= 25:
                    placa_verde()
                if placar >= 25:
                        placa_verde()
                if placar >= 50:
                    placa_verde()
            while gameloop:
                placars()
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                if fora_da_tela(groundGroup.sprites()[0]):
                    groundGroup.remove(groundGroup.sprites()[0])
                    newGround = Ground(largura - 40)
                    groundGroup.add(newGround)

                if fora_da_tela(obstacleGroup.sprites()[0]):
                    obstacleGroup.remove(obstacleGroup.sprites()[0])
                    newObstacle = posicaoAleatoriaObstaculos(largura * 1.5)
                    obstacleGroup.add(newObstacle)
                    novaMoeda = posicaoAleatoriaRubi(largura * 2)
                    novaMoeda1 = posicaoAleatoriaRubi(largura * 2.2)
                    novaMoeda2 = posicaoAleatoriaRubi(largura * 2.4)
                    novaMoeda3 = posicaoAleatoriaRubi(largura * 2.6)
                    novaMoeda4 = posicaoAleatoriaRubi(largura * 2.8)
                    grupoRubi.add(novaMoeda)
                    grupoRubi.add(novaMoeda1)
                    grupoRubi.add(novaMoeda2)
                    grupoRubi.add(novaMoeda3)
                    grupoRubi.add(novaMoeda4)

                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    velocidade = 0 # bloqueio do chaooo
                    print('Velocidade em 0')
                else:
                    velocidade = 12

                if pygame.sprite.groupcollide(playerGroup, grupoRubi, False, True):
                    placar += 1
                    pygame.mixer.Sound.play(somMoeda)


                if placar % 5 == 0 and placar != 0:
                    velocidadeJogo += 0.20
                    print('velocidade ALTERADA')

                if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
                    pygame.mixer.Sound.play(somColisao)
                    pygame.mixer.Sound.stop( trilhaSonora2 )
                    pygame.mixer.Sound.stop( trilhaSonora3 )
                    pygame.mixer.Sound.stop( trilhaSonora1 )
                    pyautogui.sleep(1)
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Não foi dessa vez !!", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(35).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(645, 400))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(645, 480))
                                tela.blit(PT, CPT)
                        L = pygame.image.load(f'{sprite}perdeu.png')
                        tela.blit(L,(0,0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_04f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()

                        pygame.display.update()
                if placar == 100:
                    while True:
                        USER = pygame.mouse.get_pos()
                        tela.fill("white")
                        S2 = pygame.image.load(f'{sprite}END.png')
                        tela.blit(S2,(-50,0))
                        L = pygame.image.load(f'{sprite}ganhou_2.png')
                        tela.blit(L,(0,0))
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(DR).png"), pos=(1183, 690),
                                    input_texto="Sair", fonte=gerarFonte(25), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(USER)
                        vVoltar.update(tela)
                        nov = Button(imagem=pygame.image.load(f"{sprite}(ES).png"), pos=(103, 690),
                                    input_texto="Novamente ", fonte=gerarFonte(18), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        nov.changeColor(USER)
                        nov.update(tela)

                        textoOPCOES = gerarFonte(35).render("Parabéns", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(645, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)

                        with open(f'{pontuacaoAT}pontuacaoAtual.txt','w') as pont:
                            d = str(placar)
                            pont.write(d)
                            with open(f'{pontuacaoAT}pontuacaoAtual.txt','r') as pont:
                                dds = pont.readlines()
                                namePT = gerarFonte(31).render(f"Pontuação atual :" , True, "Black")
                                CnamePT = namePT.get_rect(center=(980, 170))
                                tela.blit(namePT, CnamePT)
                                PT = gerarFonte(50).render(f"{d}" , True, "Black")
                                CPT = PT.get_rect(center=(980, 240))
                                tela.blit(PT, CPT)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if nov.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    Mundo_04f()
                                if vVoltar.checkForInput(USER):
                                    pygame.mixer.Sound.stop(trilhaSonora2)
                                    pygame.mixer.Sound.play(musicaInicio)
                                    Mundo_dificil()
                        pygame.display.update()
                update()
                draw()
                pygame.display.update()

        while True:
                    botaoOPCOES = pygame.mouse.get_pos()
                    tela.fill("white")
                    textoOPCOES = gerarFonte(35).render("Selecione o Mundo", True, "Black")
                    retanguloOPCOES = textoOPCOES.get_rect(center=(670, 80))
                    tela.blit(textoOPCOES, retanguloOPCOES)

                    M1 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_1.png"), pos=(280, 254),
                                        input_texto="", fonte=gerarFonte(00), corBase="white", corSobreposicao="white")
                    M1.changeColor(botaoOPCOES)
                    M1.update(tela)
                    M2 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_2.png"), pos=(935, 254),
                                        input_texto="", fonte=gerarFonte(0), corBase="white", corSobreposicao="white")
                    M2.changeColor(botaoOPCOES)
                    M2.update(tela)
                    M3 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_3.png"), pos=(309, 560),
                                        input_texto="", fonte=gerarFonte(0), corBase="#00BFFF", corSobreposicao="#32CD32")
                    M3.changeColor(botaoOPCOES)
                    M3.update(tela)
                    M4 = Button(imagem=pygame.image.load(f"{mhundo}Mundo_4.png"), pos=(950, 537),
                                        input_texto="", fonte=gerarFonte(0), corBase="#00BFFF", corSobreposicao="#FF8C00")
                    M4.changeColor(botaoOPCOES)
                    M4.update(tela)


                    voltarr = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(70, 27),
                                    input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                    voltarr.changeColor(botaoOPCOES)
                    voltarr.update(tela)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if M1.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_01f()
                            if M2.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_02f()
                            if M3.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_03f()
                            if M4.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                Mundo_04f()
                            if voltarr.checkForInput(botaoOPCOES):
                                pygame.mixer.Sound.stop(musicaInicio)
                                nivel()
                    pygame.display.update()


    def ranking():
                def server():
                    msgFromServer       = "Hello UDP Client"
                    bytesToSend         = str.encode(msgFromServer)
                    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                    UDPServerSocket.bind(("192.168.0.100" , 20030 ))
                    bytesAddressPair = UDPServerSocket.recvfrom( 1024 )
                    message = bytesAddressPair[0]
                    address = bytesAddressPair[1]
                    print(f" Pontos | {message}")
                    # with open('Pontuação.txt' ,'w') as pt:
                    #     message = str(message)
                    #     pt.write(message)
                    UDPServerSocket.sendto(bytesToSend, address)


                    while True:
                        Ranking = pygame.mouse.get_pos()
                        tela.fill("white")
                        vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                    input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        vVoltar.changeColor(Ranking)
                        vVoltar.update(tela)

                        textoOPCOES = gerarFonte(35).render("Ranking Global", True, "Black")
                        retanguloOPCOES = textoOPCOES.get_rect(center=(640, 80))
                        tela.blit(textoOPCOES, retanguloOPCOES)



                        # serv = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 427),
                        #             input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                        # serv.changeColor(Ranking)
                        # serv.update(tela)

                        jg1 = gerarFonte(26).render(f"1 - Player {message}" , True, "Black")
                        retanguloOPCOES = jg1.get_rect(center=(150, 210))
                        tela.blit(jg1, retanguloOPCOES)




                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if vVoltar.checkForInput(Ranking):
                                    pygame.mixer.Sound.stop(musicaInicio)
                                    menuPrincipal()
                                # if serv.checkForInput(Ranking):
                                #     pygame.mixer.Sound.stop(musicaInicio)
                                #     chamada()

                        pygame.display.update()





                def chamada():
                                localIP     = "192.168.0.100"
                                msg = "_"
                                bytesToSend         = str.encode(msg)
                                serverAddressPort   = (localIP, 2001)
                                bufferSize          = 1024
                                UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                                UDPClientSocket.sendto(bytesToSend, serverAddressPort)
                                UDPClientSocket.recvfrom(bufferSize)
                                server()
                chamada()

    def Story():
        def convite():
                       while True:
                            Ranking = pygame.mouse.get_pos()
                            tela.fill("white")
                            S1 = pygame.image.load(f'{sprite}convite.png')
                            tela.blit(S1,(0,0))
                            vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                        input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            vVoltar.changeColor(Ranking)
                            vVoltar.update(tela)

                            antes = Button(imagem=pygame.image.load(f"{sprite}seta_1.png"), pos=(515, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            antes.changeColor(Ranking)
                            antes.update(tela)
                            depois = Button(imagem=pygame.image.load(f"{sprite}Go.png"), pos=(765, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            depois.changeColor(Ranking)
                            depois.update(tela)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if vVoltar.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        menuPrincipal()
                                    if antes.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap3_3()
                                    if depois.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        nivel()
                            pygame.display.update()
        def cap3_3():
                       while True:
                            Ranking = pygame.mouse.get_pos()
                            tela.fill("white")
                            S1 = pygame.image.load(f'{sprite}cap3_3.png')
                            tela.blit(S1,(0,0))
                            vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                        input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            vVoltar.changeColor(Ranking)
                            vVoltar.update(tela)

                            antes = Button(imagem=pygame.image.load(f"{sprite}seta_1.png"), pos=(515, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            antes.changeColor(Ranking)
                            antes.update(tela)
                            depois = Button(imagem=pygame.image.load(f"{sprite}seta_2.png"), pos=(765, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            depois.changeColor(Ranking)
                            depois.update(tela)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if vVoltar.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        menuPrincipal()
                                    if antes.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap3_2()
                                    if depois.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        convite()
                            pygame.display.update()
        def cap3_2():
                       while True:
                            Ranking = pygame.mouse.get_pos()
                            tela.fill("white")
                            S1 = pygame.image.load(f'{sprite}cap3_2.png')
                            tela.blit(S1,(0,0))
                            vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                        input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            vVoltar.changeColor(Ranking)
                            vVoltar.update(tela)

                            antes = Button(imagem=pygame.image.load(f"{sprite}seta_1.png"), pos=(515, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            antes.changeColor(Ranking)
                            antes.update(tela)
                            depois = Button(imagem=pygame.image.load(f"{sprite}seta_2.png"), pos=(765, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            depois.changeColor(Ranking)
                            depois.update(tela)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if vVoltar.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        menuPrincipal()
                                    if antes.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap3_1()
                                    if depois.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap3_3()
                            pygame.display.update()
        def cap3_1():
                       while True:
                            Ranking = pygame.mouse.get_pos()
                            tela.fill("white")
                            S1 = pygame.image.load(f'{sprite}cap3_1.png')
                            tela.blit(S1,(0,0))
                            vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                        input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            vVoltar.changeColor(Ranking)
                            vVoltar.update(tela)

                            antes = Button(imagem=pygame.image.load(f"{sprite}seta_1.png"), pos=(515, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            antes.changeColor(Ranking)
                            antes.update(tela)
                            depois = Button(imagem=pygame.image.load(f"{sprite}seta_2.png"), pos=(765, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            depois.changeColor(Ranking)
                            depois.update(tela)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if vVoltar.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        menuPrincipal()
                                    if antes.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap2_3()
                                    if depois.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap3_2()
                            pygame.display.update()
        def cap2_3():
                       while True:
                            Ranking = pygame.mouse.get_pos()
                            tela.fill("white")
                            S1 = pygame.image.load(f'{sprite}cap2_3.png')
                            tela.blit(S1,(0,0))
                            vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                        input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            vVoltar.changeColor(Ranking)
                            vVoltar.update(tela)

                            antes = Button(imagem=pygame.image.load(f"{sprite}seta_1.png"), pos=(515, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            antes.changeColor(Ranking)
                            antes.update(tela)
                            depois = Button(imagem=pygame.image.load(f"{sprite}seta_2.png"), pos=(765, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            depois.changeColor(Ranking)
                            depois.update(tela)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if vVoltar.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        menuPrincipal()
                                    if antes.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap2_2()
                                    if depois.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap3_1()
                            pygame.display.update()
        def cap2_2():
                       while True:
                            Ranking = pygame.mouse.get_pos()
                            tela.fill("white")
                            S1 = pygame.image.load(f'{sprite}cap2_2.png')
                            tela.blit(S1,(0,0))
                            vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                        input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            vVoltar.changeColor(Ranking)
                            vVoltar.update(tela)

                            antes = Button(imagem=pygame.image.load(f"{sprite}seta_1.png"), pos=(515, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            antes.changeColor(Ranking)
                            antes.update(tela)
                            depois = Button(imagem=pygame.image.load(f"{sprite}seta_2.png"), pos=(765, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            depois.changeColor(Ranking)
                            depois.update(tela)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if vVoltar.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        menuPrincipal()
                                    if antes.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap2_1()
                                    if depois.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap2_3()
                            pygame.display.update()
        def cap2_1():
            while True:
                            Ranking = pygame.mouse.get_pos()
                            tela.fill("white")
                            S1 = pygame.image.load(f'{sprite}cap2_1.png')
                            tela.blit(S1,(0,0))
                            vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                        input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            vVoltar.changeColor(Ranking)
                            vVoltar.update(tela)

                            antes = Button(imagem=pygame.image.load(f"{sprite}seta_1.png"), pos=(515, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            antes.changeColor(Ranking)
                            antes.update(tela)
                            depois = Button(imagem=pygame.image.load(f"{sprite}seta_2.png"), pos=(765, 660),
                                        input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                            depois.changeColor(Ranking)
                            depois.update(tela)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if vVoltar.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        menuPrincipal()
                                    if antes.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap1()
                                    if depois.checkForInput(Ranking):
                                        pygame.mixer.Sound.stop(musicaInicio)
                                        cap2_2()
                            pygame.display.update()
        def cap1():
                while True:
                    Ranking = pygame.mouse.get_pos()
                    tela.fill("white")
                    S1 = pygame.image.load(f'{sprite}cap1.png')
                    tela.blit(S1,(0,0))
                    vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                    vVoltar.changeColor(Ranking)
                    vVoltar.update(tela)
                    cap1 = Button(imagem=pygame.image.load(f"{sprite}seta_2.png"), pos=(765, 660),
                                input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                    cap1.changeColor(Ranking)
                    cap1.update(tela)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if vVoltar.checkForInput(Ranking):
                               pygame.mixer.Sound.stop(musicaInicio)
                               menuPrincipal()
                            if cap1.checkForInput(Ranking):
                               pygame.mixer.Sound.stop(musicaInicio)
                               cap2_1()

                    pygame.display.update()
        cap1()


    def nivel():
            while True:
                botaoOPCOES = pygame.mouse.get_pos()
                tela.fill("white")
                tak = pygame.image.load(f'{sprite}mold.png').convert_alpha()
                tela.blit(tak,(0, 0))
                textoOPCOES = gerarFonte(35).render("Selecione o nível de dificuldade", True, "Black")
                retanguloOPCOES = textoOPCOES.get_rect(center=(640, 80))
                tela.blit(textoOPCOES, retanguloOPCOES)

                cop1 = Button(imagem=None, pos=(663, 244),
                                    input_texto="Fácil", fonte=gerarFonte(46), corBase="white", corSobreposicao="white")
                cop1.changeColor(botaoOPCOES)
                cop1.update(tela)
                Facil = Button(imagem=None, pos=(663, 244),
                                    input_texto="Fácil", fonte=gerarFonte(45), corBase="#00BFFF", corSobreposicao="#32CD32")
                Facil.changeColor(botaoOPCOES)
                Facil.update(tela)



                cop2 = Button(imagem=None, pos=(648, 376),
                                    input_texto="Médio", fonte=gerarFonte(46), corBase="white", corSobreposicao="white")
                cop2.changeColor(botaoOPCOES)
                cop2.update(tela)
                medio = Button(imagem=None, pos=(648, 376),
                                    input_texto="Médio", fonte=gerarFonte(45), corBase="#00BFFF", corSobreposicao="#FF8C00")
                medio.changeColor(botaoOPCOES)
                medio.update(tela)



                cop3 = Button(imagem=None, pos=(663, 520),
                                    input_texto="Difícil", fonte=gerarFonte(35), corBase="white", corSobreposicao="white")
                cop3.changeColor(botaoOPCOES)
                cop3.update(tela)
                Dificil = Button(imagem=None, pos=(663, 520),
                                    input_texto="Difícil", fonte=gerarFonte(34), corBase="#00BFFF", corSobreposicao="#8B0000")
                Dificil.changeColor(botaoOPCOES)
                Dificil.update(tela)


                voltarr = Button(imagem=pygame.image.load(f"{sprite}(voltar_2).png"), pos=(78, 692),
                                input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                voltarr.changeColor(botaoOPCOES)
                voltarr.update(tela)

                bixin1 = pygame.image.load(f'{sprite}v3.png')
                t1k = pygame.transform.scale(bixin1, [200 , 210])
                t11k = pygame.transform.rotate(t1k, -27)
                tela.blit(t11k,(1000,398))
                bixin2 = pygame.image.load(f'{sprite}002.png')
                t2k = pygame.transform.scale(bixin2, [400 , 500])
                tela.blit(t2k,(0,100))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Facil.checkForInput(botaoOPCOES):
                            pygame.mixer.Sound.stop(musicaInicio)
                            Mundo_facil()
                        if medio.checkForInput(botaoOPCOES):
                            pygame.mixer.Sound.stop(musicaInicio)
                            Mundo_medio()
                        if Dificil.checkForInput(botaoOPCOES):
                            pygame.mixer.Sound.stop(musicaInicio)
                            Mundo_dificil()
                        if voltarr.checkForInput(botaoOPCOES):
                            pygame.mixer.Sound.stop(musicaInicio)
                            menuPrincipal()
                pygame.display.update()
    def opcoes():
        while True:
            botaoOPCOES = pygame.mouse.get_pos()

            tela.fill("white")
            def users():
                while True:
                    USER = pygame.mouse.get_pos()
                    tela.fill("white")
                    vVoltar = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
                    vVoltar.changeColor(USER)
                    vVoltar.update(tela)

                    textoOPCOES = gerarFonte(35).render("Usuário", True, "Black")
                    retanguloOPCOES = textoOPCOES.get_rect(center=(640, 80))
                    tela.blit(textoOPCOES, retanguloOPCOES)

                    textoNome = gerarFonte(30).render("Nome :", True, "Black")
                    retanguloNome = textoNome.get_rect(center=(200, 180))
                    tela.blit(textoNome, retanguloNome)

                    NomeUser = gerarFonte(28).render(usuario, True, "Black")
                    retanguloNomeUser = NomeUser.get_rect(center=(480, 180))
                    tela.blit(NomeUser, retanguloNomeUser)



                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if vVoltar.checkForInput(USER):
                               opcoes()

                    pygame.display.update()


            textoOPCOES = gerarFonte(35).render("Objetivo :", True, "Black")
            retanguloOPCOES = textoOPCOES.get_rect(center=(640, 80))
            tela.blit(textoOPCOES, retanguloOPCOES)
            textoOPCOES2 = gerarFonte(25).render("* Adquirir 100 Rubis", True, "Black")
            retanguloOPCOES2 = textoOPCOES2.get_rect(center=(255, 133))
            tela.blit(textoOPCOES2, retanguloOPCOES2)

            textoTeclas = gerarFonte(35).render("Controles/Teclas: ", True, "Black")
            retanguloTeclas = textoTeclas.get_rect(center=(640, 247))
            tela.blit(textoTeclas, retanguloTeclas)

            textoPular = gerarFonte(25).render("- Pular: Barra de Espaço", True, "Black")
            retanguloDesenvolvedores = textoPular.get_rect(center=(325, 300))
            tela.blit(textoPular, retanguloDesenvolvedores)

            textoParar = gerarFonte(25).render("- Parar: A", True, "Black")
            retanguloDesenvolvedores = textoParar.get_rect(center=(150, 360))
            tela.blit(textoParar, retanguloDesenvolvedores)

            textoParar = gerarFonte(25).render("- Acelerar: D", True, "Black")
            retanguloDesenvolvedores = textoParar.get_rect(center=(185, 420))
            tela.blit(textoParar, retanguloDesenvolvedores)

            ################### Desenvolvedores ###################

            textoDesenvolvedores = gerarFonte(35).render("Desenvolvedores :", True, "Black")
            retanguloDesenvolvedores = textoDesenvolvedores.get_rect(center=(640, 480))
            tela.blit(textoDesenvolvedores, retanguloDesenvolvedores)

            t1 = gerarFonte(25).render("- Gabriel de Freitas", True, "Black")
            retanguloDesenvolvedores = t1.get_rect(center=(270, 540))
            tela.blit(t1, retanguloDesenvolvedores)

            t2 = gerarFonte(25).render("- Hellen Lima", True, "Black")
            retanguloDesenvolvedores = t2.get_rect(center=(184, 600))
            tela.blit(t2, retanguloDesenvolvedores)

            t3 = gerarFonte(25).render("- Júlia Araújo", True, "Black")
            retanguloDesenvolvedores = t3.get_rect(center=(198, 660))
            tela.blit(t3, retanguloDesenvolvedores)




            user = Button(imagem=pygame.image.load(f"{sprite}(USER).png"), pos=(1244, 40),
                                input_texto="", fonte=gerarFonte(45), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
            user.changeColor(botaoOPCOES)
            user.update(tela)
            poun = Button(imagem=pygame.image.load(f"{sprite}poun.png"), pos=(957, 650),
                                input_texto="", fonte=gerarFonte(5), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
            poun.changeColor(botaoOPCOES)
            poun.update(tela)
            t4 = gerarFonte(20).render("Pontuação da Atual", True, "Black")
            retanguloDesenvolvedores = t4.get_rect(center=(1045, 543))
            tela.blit(t4, retanguloDesenvolvedores)
            with open('C:\\Users\\Hellenilda\\Documents\\Algoritmos\\Python\\Jingle Grand Hero 24-11\\resultado\\pontuacaoAtual.txt','r') as arquivoAtual:
                pp = arquivoAtual.read()
                t5 = gerarFonte(80).render( pp , True, "white")
                retanguloDesenvolvedores = t5.get_rect(center=(1040, 650))
                tela.blit(t5, retanguloDesenvolvedores)

            son_of = Button(imagem=pygame.image.load(f"{sprite}(MUTE).png"), pos=(1244, 191),
                                input_texto="", fonte=gerarFonte(45), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
            son_of.changeColor(botaoOPCOES)
            son_of.update(tela)
            son_on = Button(imagem=pygame.image.load(f"{sprite}(SUND).png"), pos=(1244, 115),
                                input_texto="", fonte=gerarFonte(45), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
            son_on.changeColor(botaoOPCOES)
            son_on.update(tela)
            botaoVoltarOPCOES = Button(imagem=pygame.image.load(f"{sprite}(saida_2).png"), pos=(75, 27),
                                input_texto="<-", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")

            botaoVoltarOPCOES.changeColor(botaoOPCOES)
            botaoVoltarOPCOES.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botaoVoltarOPCOES.checkForInput(botaoOPCOES):
                        pygame.mixer.Sound.stop(musicaInicio)
                        menuPrincipal()
                    if user.checkForInput(botaoOPCOES):
                        users()
                    if son_of.checkForInput(botaoOPCOES):
                        sond_off()
                    if son_on.checkForInput(botaoOPCOES):
                        sond_on()

            pygame.display.update()
    def menuPrincipal():
        pygame.mixer.Sound.play(musicaInicio)

        while True:
            fundinho = pygame.transform.scale(backgroundMenu, [1280 , 720])
            tela.blit(fundinho , (0, 0))

            tituloMenu = pygame.mouse.get_pos()

            # logo = pygame.image.load(f'{sprite}logo.png')
            # posLogo = tela.blit(logo, (285,0))                Loguito..kkkkk   #################################################################

            botaoPLAY = Button(imagem=pygame.image.load(f"{sprite}(DR).png"),pos=(1176, 688),
                                input_texto="Ir", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9") # corBase era - bf062e
            botaoOPCOES = Button(imagem=pygame.image.load(f"{sprite}(catraca).png"),pos=(1243, 37),
                               input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
            botaoSair = Button(imagem=pygame.image.load(f"{sprite}(ES).png"),pos=(105, 688), #(250, 600)
                                input_texto="Sair", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")
            #tela.blit(logo, posLogo)    #######################################################################################################
            L = pygame.image.load(f'{sprite}JGH.png')
            LL= pygame.transform.scale(L, [610 , 620])
              #  t11k = pygame.transform.rotate(t1k, -27)
            tela.blit(LL,(390,100))

            pontosss = Button(imagem=pygame.image.load(f"{sprite}rank.png"),pos=(40, 37),
                               input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")

            STL = Button(imagem=pygame.image.load(f"{sprite}livro_atualizado.png"),pos=(1243, 140),
                               input_texto="", fonte=gerarFonte(35), corBase="#FFFAFA", corSobreposicao="#A9A9A9")


            for button in [botaoPLAY, botaoOPCOES, botaoSair, pontosss, STL]:
                button.changeColor(tituloMenu)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botaoPLAY.checkForInput(tituloMenu):
                        pygame.mixer.Sound.play(somBotao)
                        nivel()
                    if botaoOPCOES.checkForInput(tituloMenu):
                        pygame.mixer.Sound.play(somBotao)
                        opcoes()
                    if STL.checkForInput(tituloMenu):
                        pygame.mixer.Sound.play(somBotao)
                        Story()
                    if pontosss.checkForInput(tituloMenu):
                        pygame.mixer.Sound.play(somBotao)
                        ranking()
                    if botaoSair.checkForInput(tituloMenu):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
    menuPrincipal()


th.Thread(target = main).start()
Hosth()
