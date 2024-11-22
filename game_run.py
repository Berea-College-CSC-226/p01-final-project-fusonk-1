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
from player import *

import pygame



class Game:
    def __init__(self):
        """
        Handles the basic logic needed to actually run the game
        """
        pygame.init()
        self.size = (200,200) #Window size
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('white')
        self.red_block = Player(self.size)

    def game_loop(self):
        """
        Handles running the game
        :return:
        """
        run = True
        while run:
            self.screen.fill('gray')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     run = False
        self.red_block.movement(pygame.key.get_pressed())
        self.screen.blit(self.red_block.surf, self.red_block.rect)

        pygame.display.update()

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
    game.game_loop()

if __name__ == "__main__":
    main()