import pygame

#############################
# Initialize pygame
#############################
pygame.init()

#############################
# Constants
#############################
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255,165,0)

#############################
# Image
#############################
background = pygame.image.load('image/background.jpg')
logo = pygame.image.load('image/logo_text.png')
icon = pygame.image.load('image/logo.png')
pointer = pygame.image.load('image/pointer.png')

#############################
# Font
#############################
font_bold = pygame.font.Font('font/TurretRoad-Bold.ttf', 40)
font = pygame.font.Font('font/TurretRoad-Regular.ttf', 30)

#############################
# Game Display Setting
#############################
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Congklak")
pygame.display.set_icon(icon)


#############################
# Global Variable
#############################
value_option = 0

#############################
# Start Screen
#############################
def showStartScreen():
    global value_option

    option_selected = False
    while not option_selected:
        #### Show background image ####
        display.blit(background, (0,0))

        #### Show logo ####
        logo_location_x = WIDTH/2 - logo.get_rect().width/2
        logo_location_y = HEIGHT/2 - logo.get_rect().height - 50
        display.blit(logo, (logo_location_x,logo_location_y))

        #### Show title ####
        title = font_bold.render('Congklak Asik', True, ORANGE)
        title_location_x = WIDTH/2 - title.get_rect().width/2
        title_location_y = HEIGHT/2 - 50
        display.blit(title, (title_location_x, title_location_y))

        #### Show Option WHO is PLAYING ####
        playing_options = ['PLAYER vs AI', 'PLAYER vs BOT', 'AI vs BOT']
        for option in range(0, len(playing_options)):
            option_text = font.render(playing_options[option], True, ORANGE)
            display.blit(option_text, (title_location_x, title_location_y + 100 + option*50))

        #### Show pointer for selecting option ####
        display.blit(pointer, (title_location_x - 50, title_location_y + 100 + value_option*50))

        #### Controller Handler ####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                ## ARROW DOWN PRESSED ###
                if event.key == pygame.K_DOWN:
                    if value_option == len(playing_options) - 1:
                        value_option = 0
                    else:
                        value_option += 1    
                ## ARROW UP PRESSED ###
                if event.key == pygame.K_UP:
                    if value_option == 0:
                        value_option = len(playing_options) - 1
                    else:
                        value_option -= 1
                ### ENTER PRESSED ###
                if event.key == pygame.K_RETURN:
                    option_selected = True
                    
        #### Update Display ####
        pygame.display.update()

#############################
# Gameplay
#############################
def gameLoop():
    global value_option
    print(value_option)
    while True:
        #### Show background image ####
        display.blit(background, (0,0))

        #### Controller Handler ####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                ## ARROW RIGHT PRESSED ##
                if event.key == pygame.K_RIGHT:
                    pass
                ## ARROW LEFT PRESSED ##
                if event.key == pygame.K_LEFT:
                    pass

        #### Update Display ####
        pygame.display.update()
        
#############################
# Finish Screen
#############################
def showFinishScreen():
    pass    

#############################
# Run the game
#############################
showStartScreen()
gameLoop()
# showFinishScreen()