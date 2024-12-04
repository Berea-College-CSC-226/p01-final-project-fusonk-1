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
# https://www.pygame.org/docs/ref/display.html for updating display, as well as just general pygame tools
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
from player import *
from monster import *
import pygame



class Game:
    def __init__(self):
        """
        Handles the basic logic needed to actually run the game
        """
        pygame.init()
        self.size = (200,200) #Window size
        self.screen = pygame.display.set_mode(self.size)
        self.player = Player(self.size)
        self.monster = Monster(self.size)
        self.chest = Item(self.size)
        # self.hp = Monster(self.health)
        # self.health = Monster(self.health)
        # self.attack = Monster(self.damage)
        self.damage = 1


    def game_loop(self, damage):
        """
        Handles running the game
        :return:
        """
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill('gray')
            self.player.movement(pygame.key.get_pressed())
            keys = pygame.key.get_pressed()  # Get currently pressed keys
            self.player.movement(keys)  # Update player position based on keys
            self.screen.blit(self.player.surf, self.player.rect)  #spawn player
            self.screen.blit(self.monster.surf, self.monster.rect) #spawns monster
            self.screen.blit(self.chest.surf, self.chest.rect)  # spawns chest

            #Collision Interaction - Player damages Monster
            if pygame.sprite.spritecollide(self.player, self.monster, dokill = False):
                if keys[pygame.K_f]:
                    hp = Monster.take_damage(self.monster, damage)
                    hp()

            pygame.display.update() #updates the screen to fix screen turning black

    def game_over(self):
        """
        checks if game is over
        :return:
        """
        pass

    def display_stats(self):
        """
        displays information on screen such as gold, health, and item
        :return:
        """



        pygame.quit()

def main():
    """
    Starts the dungeon crawler

    :return: None
    """
    game = Game()
    # pygame.display.update()
    game.game_loop(game.damage)


if __name__ == "__main__":
    main()