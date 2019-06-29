
import sys , pygame

def check_keydown_events(event,ai_settings,screen,character_A):
    
        if event.key == pygame.K_RIGHT:
            character_A.moving_right = True      
        elif event.key == pygame.K_LEFT: 
            character_A.moving_left = True


def check_keyup_events(event,character_A):            
    if event.key == pygame.K_RIGHT:
        character_A.moving_right = False      
    elif event.key == pygame.K_LEFT: 
        character_A.moving_left = False   

def check_events(ai_settings,screen,character_A):
    # Respond to keypresse and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN:
             check_keydown_events(event,ai_settings,screen,character_A)

        elif event.type == pygame.KEYUP:
              check_keyup_events(event,character_A)

def update_screen(ai_settings, screen ,character_A):
    #Update images on the screen and flip to the new screen
    # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        character_A.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()
    