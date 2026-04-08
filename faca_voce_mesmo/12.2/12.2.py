# 12.1 – Céu azul: Crie uma janela do Pygame com uma cor de fundo azul.
import pygame
import sys
from personagem import Personagem


def window():
    pygame.init()
    bg_color = (0, 0, 255)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Windows Test')
    personagem = Personagem(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)        
        personagem.blitme()
        pygame.display.flip()

window()
