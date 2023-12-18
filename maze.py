import pygame, random
from maze_settings import *
from player import Player
from Tile import Tile
#from way import Way
from trap import Trap
from goal import Goal
from score import Score
from game import Game
from Music import *
class world:
        def __init__(self,world_data,screen):               
                self.screen = screen
                self.world_data = world_data
                self._setup_world(world_data)
                self.game = Game(self.screen)
                self.world_shift = 0
                self.world_shift_y = 0

                self.way_x = Width // 2 - len(self.world_data[0]) / 2 * Tile_size
                self.way_y = Height // 2 - len(self.world_data[0]) / 2 * Tile_size            

                self.player_start_cord_x
                self.player_start_cord_y
                self.trap_visible = True
                self.last_sprite_change_time = pygame.time.get_ticks()
                self.scorepoint = 10
                self.scoretake = 0
                self.Scorespawn = 0
                self.scoreall = False
                Background()

        def _setup_world(self,layout):
            
            self.tiles = pygame.sprite.Group()
            self.player = pygame.sprite.GroupSingle()
            self.way = pygame.sprite.Group()
            self.traps = pygame.sprite.Group()
            self.goal = pygame.sprite.Group()
            self.score = pygame.sprite.Group()
            center_x = Width // 2 - len(self.world_data[0]) / 2 * Tile_size
            center_y = Height // 2 - len(self.world_data) / 2 * Tile_size
        
            sc = 0
            scoreflag = True
            # 5 монеток
            moneyflag = True
            totalmoney = 1
            if (totalmoney != 0):
                if (moneyflag):
                        for i in range(5):
                                random_x = random.randint(1, len(self.world_data[0])-1) #16
                                random_y = random.randint(1, len(self.world_data)-1) #12
                                while self.world_data[random_y][random_x] != 0:
                                        random_x = random.randint(1, len(self.world_data[0])-1)
                                        random_y = random.randint(1, len(self.world_data)-1)       
                                self.world_data[random_y][random_x] = 5 
                                totalmoney-=1
                                if (totalmoney == 0):
                                        moneyflag = False
            if (scoreflag):
                for i in range(len(self.world_data)-1):
                        for j in range(len(self.world_data[i])-1):
                                if self.world_data[i][j] == 0:
                                        self.world_data[i][j] = 6
                                        sc+=1
                self.Scorespawn = sc
                
                scoreflag = False     
                               
            for i in range(len(self.world_data)):
                for j in range(len(self.world_data[i])):
                        
                        x,y = j *Tile_size + center_x, i * Tile_size + center_y
                        if self.world_data[i][j] == 2:
                                player_sprite = Player((x, y))
                                self.player.add(player_sprite)
                                self.player_start_cord_x,  self.player_start_cord_y = x, y
                                 
                        elif self.world_data[i][j] == 1:
                                tile = Tile((x, y), Tile_size)
                                self.tiles.add(tile)
                        elif self.world_data[i][j] == 4:
                                tile = Trap((x - (Tile_size // 4)+5, y - (Tile_size // 4)), Tile_size )
                                #tile = Trap((x, y), Tile_size)
                                self.traps.add(tile)
                        elif self.world_data[i][j] == 5:
                                goal = Goal((x, y), Tile_size)
                                self.goal.add(goal)   
                        if self.world_data[i][j] == 6:
                                score_sprite = Score((x, y), Tile_size)
                                self.score.add(score_sprite)
                                
                                
                        #if self.world_data[i][j] == 0 or self.world_data[i][j] == 2:
                                #pygame.draw.rect(self.screen, color_way,(j * Tile_size, i * Tile_size, Tile_size, Tile_size))
                                #way_sprite = Way((x, y), Tile_size)
                                #self.way.add(way_sprite)
                


        def draw_tile(self, x_shift, y_shift):
                center_y = Height // 2 - len(self.world_data) / 2 * Tile_size
                y = center_y
                self.way_x += x_shift
                self.way_y += y_shift
                for i in range(len(self.world_data)):
                        for j in range(len(self.world_data[i])):
                                #if self.world_data[i][j] == 0 or self.world_data[i][j] == 2 or self.world_data[i][j] == 5 or self.world_data[i][j] == 6:
                                        #pygame.draw.rect(self.screen, color_way,(j * Tile_size + self.way_x, i * Tile_size +y, Tile_size, Tile_size))
                                #elif self.world_data[i][j] == 3:
                                        #pygame.draw.rect(self.screen, color_bonus, (j * Tile_size + self.way_x, i * Tile_size + y, Tile_size, Tile_size))
                                if self.world_data[i][j] == 3:
                                        pygame.draw.rect(self.screen, color_bonus, (j * Tile_size + self.way_x, i * Tile_size + y, Tile_size, Tile_size))
                                elif self.world_data[i][j] != 1 and self.world_data[i][j] != 9: # !=1
                                        pygame.draw.rect(self.screen, color_way,(j * Tile_size + self.way_x, i * Tile_size +y, Tile_size, Tile_size))


        # движение камеры по x
        def _scroll_x(self):

                player = self.player.sprite
                player_x = player.rect.centerx
                #player_y = player.rect.centeryx
                direction_x = player.direction.x
                direction_y = player.direction.y
                if player_x < Width // 3 and direction_x < 0 and direction_y == 0:
                        self.world_shift = 5
                        player.speed = 0
                elif player_x > Width - (Width // 3) and direction_x > 0 and direction_y == 0:
                        self.world_shift = -5
                        player.speed = 0
                else:
                        self.world_shift = 0
                        #self.world_shift_y = 0
                        player.speed = 5
                
                """
                elif player_y < Height // 3 - 50 and direction_y < 0 and direction_x == 0:
                        self.world_shift_y = 5
                        player.speed = 0
                elif player_y > Height - (Height // 3)+50 and direction_y > 0 and direction_x == 0:
                        self.world_shift_y = -5
                        player.speed = 0
                        """
                

                #Слежка за игроком
                """
                if player_x < Width - (Width // 2) and direction_x < 0 and direction_y == 0:
                        self.world_shift = 5
                        player.speed = 0
                elif player_x > Width - (Width // 2) and direction_x > 0 and direction_y == 0:
                        self.world_shift = -5
                        player.speed = 0
                """
        # take goal
        def _handle_collision(self):
                player = self.player.sprite
                pygame.sprite.spritecollide(player, self.goal, True)
                
                if pygame.sprite.spritecollide(player, self.score, True):
                        self.scoretake+=1
                        if (self.scoretake == self.Scorespawn):
                                self.scoreall = True
                if pygame.sprite.spritecollide(player, self.traps, False) and self.trap_visible == True:
                        player.rect.x = self.player_start_cord_x
                        player.rect.y = self.player_start_cord_y
                        player.life -= 1
                    
        def traptime(self):
                current_time = pygame.time.get_ticks()   
                if current_time - self.last_sprite_change_time >= 5000:
                        # Если прошло 5 секунд, меняем видимость спрайта
                        self.last_sprite_change_time = current_time
                        self.trap_visible = not self.trap_visible

        # prevents player to pass through objects horizontall
        def _horizontal_movement_collision(self):
                player = self.player.sprite
                player.rect.x += player.direction.x * player.speed
                for sprite in self.tiles.sprites():
                        if sprite.rect.colliderect(player.rect):
                                # checks if moving towards left
                                if player.direction.x < 0:
                                        player.rect.left = sprite.rect.right
                                        player.direction.x = 0
                                        player.on_left = True
                                        current_x = player.rect.left
                                # checks if moving towards right
                                elif player.direction.x > 0:
                                        player.rect.right = sprite.rect.left
                                        player.on_right = True
                                        player.direction.x = 0
                                        current_x = player.rect.right
                if player.on_left and (player.rect.left < current_x or player.direction.x >= 0):
                        player.on_left = False
                if player.on_right and (player.rect.right > current_x or player.direction.x <= 0):
                        player.on_right = False

                
        # prevents player to pass through objects vertically
        def _vertical_movement_collision(self):
                player = self.player.sprite
                player.rect.y += player.direction.y * player.speed
        
                for sprite in self.tiles.sprites():
                        if sprite.rect.colliderect(player.rect):
                                # checks if moving towards bottom
                                if player.direction.y > 0:
                                        player.rect.bottom = sprite.rect.top
                                        player.direction.y = 0
                                        player.on_ground = True
                                # checks if moving towards up
                                elif player.direction.y < 0:
                                        player.rect.top = sprite.rect.bottom
                                        player.direction.y = 0
                                        player.on_ceiling = True
                if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                        player.on_ground = False
                if player.on_ceiling and player.direction.y > 0:
                        player.on_ceiling = False
                
        
        # updating the game world from all changes committed
        def update(self, player_event):
                # for tile
                self.tiles.update(self.world_shift,self.world_shift_y)
                self.tiles.draw(self.screen)
                
                # for way
                #self.way.update(self.world_shift, self.world_shift_y)
                #self.way.draw(self.screen)

                # for draw tile
                self.draw_tile(self.world_shift, self.world_shift_y)
                # for goal
                self.goal.update(self.world_shift, self.world_shift_y)
                self.goal.draw(self.screen)
                #for score
                self.score.update(self.world_shift, self.world_shift_y)
                self.score.draw(self.screen)
                # for trap
                if (self.trap_visible):                        
                        self.traps.draw(self.screen)
                self.traptime()
                self.traps.update(self.world_shift)
                # for collsion
                self._handle_collision()

                #self._scroll_x()

                
                self.player.update(player_event)
                self.player.draw(self.screen)

                self._horizontal_movement_collision()
                self._vertical_movement_collision()

                self.game.show_life(self.player.sprite)
                self.game.game_state(self.player.sprite, self.scoreall)
