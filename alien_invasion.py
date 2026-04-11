import pygame
from pygame.sprite import Group
import game_functions as gf
from alien import Alien
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from scoreboard import Scoreboard


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Ivasion')
    
    # Criar botão play
    play_button = Button(ai_settings, screen, "Play")
    
    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    
    # Cria um grupo no qual serão armazenados os projéteis 
    bullets = Group()
    aliens = Group()
    
    #Criar a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Cria a frota de alienígenas
    alien = Alien(ai_settings, screen)
    
    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:        
            ship.update()        
            bullets.update()
        
            # Livra-se dos projéteis que desapareceram
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
        
            # Redesenha a tela a cada passagem pelo laço
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        
run_game()    

