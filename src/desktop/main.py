
import sys , pygame
from pygame.locals import *
from settings_lvl1 import Settings_lvl1
from character import *
import game_functions as gf 
from pygame.sprite import Group

"""
Programming Style
 - Things
 - Pipeline
 - Letterbox

"""

def main():
    #Initialize game,settings and create a scren object.
    pygame.init()
    ai_settings = Settings_lvl1()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht,ai_settings.screen_height))

    # Make a  Assasin
    character_A = Assasin(ai_settings,screen)



    #Start the main loop fot the game
    while True:

        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings,screen,character_A)
        character_A.update()
        gf.update_screen(ai_settings,screen,character_A)

if __name__ == '__main__':
    main()


