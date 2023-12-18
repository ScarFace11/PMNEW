import pygame
import sys
from maze_settings import *
from maze import world
class Main:
    def __init__(self, screen):
        self.screen = screen          
        self.clock = pygame.time.Clock()
        self.player_event = False
        self.maze = None
        # Другие инициализации

    def main(self,mazenum):
        World = world(mazenum, self.screen) #---------
        while True:
            self.screen.fill((35, 45, 60))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player_event = 'left'
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player_event = 'right'  
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player_event = 'down'
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player_event = 'up'
                    elif event.key == pygame.K_r:
                        self.player_event = 'restart'
                          
                #elif event.type == pygame.KEYUP:
                    #self.player_event = False

             
            World.update(self.player_event) #--------
            #Menu.menu(self.player_event)         
            pygame.display.update()
            self.clock.tick(60)