######################################################################
# Author: Kirsten Fuson
# Username: fusonk
#
# Assignment: Final Project
#
# Purpose: This program is designed to test my final project
#
#
######################################################################
# Acknowledgements:
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import pygame
from player import *
from dungeon import *


class Monster:
    def __init__(self,screen_size, width=50, height=50):
        """
        Handles the basic logic needed to create monsters
        """
        super().__init__()
        self.screen_size = screen_size
        print("Spawning monster")
        self.surf = pygame.image.load('image/enemy.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.size = 5
        self.surf = pygame.transform.scale(self.surf, (width, height)) #changes height and width of monster
        self.rect.x = screen_size[0] - width  # Right of screen, changes spawn point
        self.rect.y = 0  # Top of screen, changes spawn point

    def movement(self):
        """
        Moves the characters in a pattern
        :return:
        """
        pass

    def attack_player(self, player):
        """
        calculates the monsters attack, as well as sees if the monster can attack
        :param player:
        :return:
        """
        pass

    def take_damage(self):
        """
        calculates the damage the monster takes after its been hit
        :param:
        :return:
        """
        pass
