import pygame
from player import *
from dungeon import *

class Attack:
    def __init__(self,screen_size, width=20, height=20):
        #Monster attack image
        super().__init__()
        self.screen_size = screen_size
        print("Spawning monster")
        self.surf = pygame.image.load('image/attack.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.size = 5
        self.surf = pygame.transform.scale(self.surf, (width, height))  # changes height and width of monster
        self.rect.x = screen_size[0] - width  # Right of screen, changes spawn point
        self.health = 2


    def take_damage(self, damage):
        """
        calculates the damage the monster takes after its been hit
        :param:
        :return:
        """
        #Trying to make monster take damage
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        self.rect.y = 50
        self.alive = False
        print("An attack has despawned") #just for testing purposes