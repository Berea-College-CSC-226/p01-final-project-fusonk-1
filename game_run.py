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
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect - More collision Information
#https://www.pygame.org/docs/ref/time.html#pygame.time.delay - delay/Timer
# str(self.player.hp) - converting a int into a string for display - Professor Hegan
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
from random import randint

from player import *
from monster import *
from attack import *
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
        self.attack = Attack(self.size)
        self.chest = Item(self.size)
        self.damage = 1
        self.enemy_invincible = False
        self.chest_empty = False
        self.player_invincible = False


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
            self.screen.blit(self.attack.surf, self.attack.rect)
            self.screen.blit(self.chest.surf, self.chest.rect)  # spawns chest

            # Display Text
            font = pygame.font.SysFont("ComicSans", 10)
            #Health text
            txt = font.render('Health', True, "darkblue")
            self.screen.blit(txt, (self.size[0] // 16, self.size[1] - 200)) #Division, and minus changes the place where the text spawns

            #str converts the int into a string for display
            player_health = font.render(str(self.player.hp), True, "darkblue")
            self.screen.blit(player_health,(self.size[0] // 4, self.size[1]-200))

            #Gold Text
            text = font.render('Gold', True, "darkblue")
            self.screen.blit(text, (self.size[0] //3, self.size[1] - 200))

            #converts the int into str for display
            t = font.render(str(self.chest.gold), True, "darkblue")
            self.screen.blit(t, (self.size[0]//2, self.size[1] - 200))

            #Collision Interaction - Player damages Monster
            ##tests for collision between two sprites, specifically sprites with rect function.
            if pygame.sprite.collide_rect(self.player, self.monster):  #Only this collision type works as expected, do not remove!
                   if keys[pygame.K_f]:
                       if self.enemy_invincible == False: #Checks if monster is able to be hurt
                           Monster.take_damage(self.monster, damage)
                           self.enemy_invincible = True #makes it so monster cant be hurt
                           pygame.time.delay(200) #Timer delays in milliseconds
                           self.enemy_invincible = False

            #Collision Interaction - Enemy attacks player
            if pygame.sprite.collide_rect(self.player,self.attack):
                if self.player_invincible == False:
                    Player.take_damage(self.player,damage)

                    self.player_invincible = True
                    pygame.time.delay(1000)
                    self.player_invincible = False

            #Collision Interaction - Chest and Player
            if pygame.sprite.collide_rect(self.player,self.chest):
                if keys[pygame.K_a]:
                    if self.chest_empty == False:
                        self.chest.gold += randint(20,100)
                        self.chest_empty = True


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
    game.game_loop(game.damage)  #Passed parameter into loop


if __name__ == "__main__":
    main()