# 12.1 – Céu azul: Crie uma janela do Pygame com uma cor de fundo azul.
import pygame
import sys

def window():
    pygame.init()
    scree_width = int(1200)
    scree_height = int(800)
    bg_color = (0, 0, 255)
    screen = pygame.display.set_mode((scree_width, scree_height))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        pygame.display.flip()

window()
