import pygame
import time

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
board = pygame.image.load('image/board.png')
pointer_up = pygame.image.load('image/pointer-up.png')
pointer_down = pygame.image.load('image/pointer-down.png')

#############################
# Font
#############################
big_font = pygame.font.Font('font/TurretRoad-Bold.ttf', 100)
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
# 0 = PLAYER vs AI
# 1 = PLAYER vs BOT
# 2 = AI vs BOT

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
    
    ### STATE ###
    game_on = True
    hole_selected = 0
    turn = 0
    PLAYER = 0
    AI = 1
    BOT = 2
    NUMBER_HOLES = 7

    #### PLAYER vs AI ####
    if value_option == 0:
        turn_order = [PLAYER, AI]

    #### PLAYER vs BOT ####
    if value_option == 1:
        turn_order = [PLAYER, BOT]

    #### Ai vs BOT ####
    if value_option == 2:
        turn_order = [AI, BOT]

    while game_on:
        #### Show background image ####
        display.blit(background, (0,0))

        #### Show congklak board ####
        board_location_x = WIDTH/2 - board.get_rect().width/2
        board_location_y = HEIGHT/2 - board.get_rect().height/2
        display.blit(board, (board_location_x, board_location_y))

        #### Show Turn ####
        if turn_order[turn] == PLAYER:
            turn_text = font_bold.render('PLAYER TURN', True, ORANGE)
            display.blit(turn_text, (WIDTH/2 - turn_text.get_rect().width/2, 40))
        elif turn_order[turn] == AI:
            turn_text = font_bold.render('AI TURN', True, ORANGE)
            display.blit(turn_text, (WIDTH/2 - turn_text.get_rect().width/2, 40))
        elif turn_order[turn] == BOT:
            turn_text = font_bold.render('BOT TURN', True, ORANGE)
            display.blit(turn_text, (WIDTH/2 - turn_text.get_rect().width/2, 40))

        #### Show select hole option ####
        if turn == 0:
            display.blit(pointer_up, (hole_selected*64 + 190, board_location_y + board.get_rect().height - 30))
        elif turn == 1:
            display.blit(pointer_down, (hole_selected*64 + 190, board_location_y + 10))

        #### Controller Handler ####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_on = False
                ## ARROW RIGHT PRESSED ##
                if event.key == pygame.K_RIGHT:
                    if hole_selected == NUMBER_HOLES - 1:
                        hole_selected = 0
                    else:
                        hole_selected += 1
                ## ARROW LEFT PRESSED ##
                if event.key == pygame.K_LEFT:
                    if hole_selected == 0:
                        hole_selected = NUMBER_HOLES - 1
                    else:
                        hole_selected -= 1
                ## ENTER PRESSED ##
                if event.key == pygame.K_RETURN:
                    if turn == 0:
                        turn = 1
                    elif turn == 1:
                        turn = 0 

        #### Update Display ####
        pygame.display.update()
        
#############################
# Finish Screen
#############################
def showFinishScreen():
    #### Show background ####
    pygame.draw.rect(display, BLACK, (0,0,WIDTH,HEIGHT))

    #### Show credit ####
    thank_you = big_font.render('THANK YOU!', True, WHITE)
    display.blit(thank_you, (WIDTH/2 - thank_you.get_rect().width/2, HEIGHT/2))

    #### Update Display ####
    pygame.display.update()

    time.sleep(3)
    pygame.quit()    

#############################
# Run the game
#############################
showStartScreen()
gameLoop()
# showFinishScreen()