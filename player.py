import pygame
from maze_settings import *
from support import import_sprite

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self._import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.25
        self.image = self.animations["walk"][self.frame_index]
        self.image = pygame.Surface((Tile_size,Tile_size))

        self.rect = self.image.get_rect(topleft=pos)
        #self.mask = pygame.mask.from_surface(self.image)
        
        self.direction = pygame.math.Vector2(0, 0)
        self.money = 0
        
        self.speed = 5

        self.life = 3

        self.on_left = False
        self.on_right = False
        self.on_ceiling = False
        self.on_ground = False
              
        self.status = "walk"
        self.facing_right = True
        self.facing_left = False
        self.facing_down = False
        self.facing_up = False



    def _import_character_assets(self):
        character_path = "Sprite/pacman/"
        self.animations = {"walk": []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_sprite(full_path)


    # animates the player actions
    def _animate(self):
        animation = self.animations[self.status]
        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        image = pygame.transform.scale(image, (Tile_size, Tile_size))
        if self.facing_right:
            self.image = image
        elif self.facing_left:
            flipped_image = pygame.transform.flip(image, True, False)         
            self.image = flipped_image
        elif self.facing_up:
            flipped_image =pygame.transform.rotate(image, 90)
            self.image = flipped_image
        elif self.facing_down:
            flipped_image =pygame.transform.rotate(image, 270)
            self.image = flipped_image

        # set the rect
        if self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        
    def SetValue(self):
        
        if self.oldy > self.rect.y:
            return True
        else:
            self.oldy = self.rect.y
            return False
        
    def _get_input(self, player_event):
        if player_event != False:
            if player_event == "right":
                self.direction.x = 1
                #self.direction.y = 0
                self.facing_down = False
                self.facing_up = False
                self.facing_left = False
                self.facing_right = True    
            elif player_event == "left":
                self.direction.x = -1
                #self.direction.y = 0
                self.facing_down = False
                self.facing_up = False
                self.facing_left = True
                self.facing_right = False              
            elif player_event == "up":               
                self.direction.y = -1
                #self.direction.x = 0                 
                self.facing_down = False
                self.facing_up = True
                self.facing_left = False
                self.facing_right = False
            elif player_event == "down":
                self.direction.y = 1
                #self.direction.x = 0  
                self.facing_down = True
                self.facing_up = False
                self.facing_left = False
                self.facing_right = False
            elif player_event == "restart":
                self.rect.x = 580
                self.rect.y = 485

        #else:
            #self.direction.x = 0
            #self.direction.y = 0
    # identifies player action
    def _get_status(self):
        if self.direction.x != 0:
            self.status = "walk"

    # update the player's state
    def update(self, player_event):
        self._get_status()

        self._get_input(player_event)

        self._animate()
