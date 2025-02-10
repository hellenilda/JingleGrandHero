from ast import Str
from time import sleep
import os , pygame, pyautogui as pt
def timer():
    pygame.init()
    tela = pygame.display.set_mode((180, 100))
    pygame.display.set_caption("TIME")
    tela.fill("white")
    def gerarFonte(tamanho):
            return pygame.font.Font("C:\\Users\\Robótica-LaISER\\Desktop\\Jingle Grand Hero\\20-11-2022\\sprites\\font.ttf", tamanho)
    def limpar():
            os.system('clear')
    minuto = segundo = milesimos = 0
    while True:
        xxxx = f"{minuto}:{segundo}:{milesimos}"
        print(xxxx)
        sleep(0.01)
        milesimos += 1
        if milesimos == 100:
            milesimos = 0
            segundo += 1
        if segundo == 60:
            segundo = 0
            minuto += 1
            limpar()
        if minuto == 60:
            break
        pygame.draw.rect(tela, "white", pygame.Rect(0, 0, 180, 180)) 
        pygame.display.flip() 
        Cronometro_blit2 = gerarFonte(20).render( str(xxxx) , True, "black")
        meio2 = Cronometro_blit2.get_rect(center=(90, 50))
        tela.blit(Cronometro_blit2, meio2 )
        pygame.display.update()

timer()