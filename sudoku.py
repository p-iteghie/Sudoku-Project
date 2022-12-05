import sys
import sudoku_generator as sg
from cell import Cell
from board import Board
import pygame
from constants import *

# Main Method
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    # set fonts for game
    title_font = pygame.font.Font("Luciole-Bold.ttf", 45)
    select_font = pygame.font.Font("Luciole-Regular.ttf", 35)
    mode_font = pygame.font.Font("Luciole-Bold.ttf", 25)
    option_font = pygame.font.Font("Luciole-Bold.ttf", 25)

    # set different types of text for game
    title = title_font.render("Welcome to Sudoku!", True, TEXT_COLOR)
    select = select_font.render("Select a Game Mode:", True, TEXT_COLOR)
    easy_mode = mode_font.render("EASY", True, BG_COLOR)
    medium_mode = mode_font.render("MEDIUM", True, BG_COLOR)
    hard_mode = mode_font.render("HARD", True, BG_COLOR)

    # set buttons for game
    mode_buttons_border = [pygame.Rect((WIDTH - BUTTON_WIDTH) / 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT),
                           pygame.Rect((WIDTH - BUTTON_WIDTH) / 2, 400 + BUTTON_HEIGHT + 20, BUTTON_WIDTH,
                                       BUTTON_HEIGHT),
                           pygame.Rect((WIDTH - BUTTON_WIDTH) / 2, 400 + (BUTTON_HEIGHT + 20) * 2, BUTTON_WIDTH,
                                       BUTTON_HEIGHT)]

    easy_button = pygame.Rect((WIDTH - BUTTON_WIDTH + BUTTON_BORDER) / 2, 400 + BUTTON_BORDER / 2,
                              BUTTON_WIDTH - BUTTON_BORDER, BUTTON_HEIGHT - BUTTON_BORDER)
    medium_button = pygame.Rect((WIDTH - BUTTON_WIDTH + BUTTON_BORDER) / 2,
                                400 + BUTTON_BORDER / 2 + BUTTON_HEIGHT + 20, BUTTON_WIDTH - BUTTON_BORDER,
                                BUTTON_HEIGHT - BUTTON_BORDER)
    hard_button = pygame.Rect((WIDTH - BUTTON_WIDTH + BUTTON_BORDER) / 2,
                              400 + BUTTON_BORDER / 2 + (BUTTON_HEIGHT + 20) * 2, BUTTON_WIDTH - BUTTON_BORDER,
                              BUTTON_HEIGHT - BUTTON_BORDER)

    # set buttons for reset, restart, and exit for the user
    reset_option = option_font.render("RESET", True, BG_COLOR)
    restart_option = option_font.render("RESTART", True, BG_COLOR)
    exit_option = option_font.render("EXIT", True, BG_COLOR)

    screen_type = 'welcome_screen'
    
    while True:
      # The action listener for the program. Will check if a user presses: the return key, a mouse click,
      # or if the window is exitted
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_type == 'welcome_screen':  # selects game difficulty
                    if easy_button.collidepoint(event.pos):
                        pygame.time.wait(200)
                        board = Board(WIDTH, HEIGHT, screen, 1)
                        screen_type = 'play_game'
                    elif medium_button.collidepoint(event.pos):
                        pygame.time.wait(200)
                        board = Board(WIDTH, HEIGHT, screen, 2)
                        screen_type = 'play_game'
                    elif hard_button.collidepoint(event.pos):
                        pygame.time.wait(200)
                        board = Board(WIDTH, HEIGHT, screen, 3)
                        screen_type = 'play_game'
                elif screen_type == 'play_game' or screen_type == 'lose_screen' or screen_type == 'win_screen':
                    if reset_button.collidepoint(event.pos):  # clears the board
                        for box in board.cell_list:
                            if box.editable:
                                box.sketch, box.value = 0, 0
                    if restart_button.collidepoint(event.pos):  # returns Game Start screen
                        screen_type = 'welcome_screen'
                    if exit_button.collidepoint(event.pos):  # ends the program
                        pygame.quit()
                        sys.exit()
                    for box in board.cell_list:
                        if box.cell.collidepoint(event.pos) and box.editable:
                            for other_box in board.cell_list:  # ensures only one cell is highlighted
                                other_box.color = CELL_BORDER_UNHIGHLIGHTED
                            box.color = CELL_BORDER_HIGHLIGHTED
            if event.type == pygame.KEYDOWN:
                if screen_type == 'play_game':
                    for box in board.cell_list:
                        if box.color == CELL_BORDER_HIGHLIGHTED:
                            if event.unicode in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                box.sketch = event.unicode
                            if event.key == pygame.K_RETURN:
                                if box.sketch != 0:
                                    box.set_cell_value(box.sketch)
                                    box.sketch = 0
                        if board.is_filled() and screen_type == 'play_game':
                            if board.check_win():
                                screen_type = 'win_screen'
                            else:
                                screen_type = 'lose_screen'

        screen.fill(BG_COLOR)

        # home screen with difficulty options
        if screen_type == 'welcome_screen':  
            screen.blit(title, ((WIDTH - title.get_rect().width) / 2, 100))
            screen.blit(select, ((WIDTH - select.get_rect().width) / 2, 350))

            # creates a border for the buttons
            for button in mode_buttons_border:  
                pygame.draw.rect(screen, TEXT_COLOR, button)

            # draws buttons 
            pygame.draw.rect(screen, BUTTON_COLOR, easy_button)
            pygame.draw.rect(screen, BUTTON_COLOR, medium_button)
            pygame.draw.rect(screen, BUTTON_COLOR, hard_button)

            # adds text to buttons
            screen.blit(easy_mode, (
                (WIDTH - easy_mode.get_rect().width) / 2, 400 + (BUTTON_HEIGHT - easy_mode.get_rect().height) / 2))
            screen.blit(medium_mode, ((WIDTH - medium_mode.get_rect().width) / 2,
                                      400 + BUTTON_HEIGHT + 20 + (BUTTON_HEIGHT - easy_mode.get_rect().height) / 2))
            screen.blit(hard_mode, ((WIDTH - hard_mode.get_rect().width) / 2,
                                    400 + (BUTTON_HEIGHT + 20) * 2 + (BUTTON_HEIGHT - easy_mode.get_rect().height) / 2))

        # draws interactive sudoku board
        if screen_type == 'play_game':  
            board.draw()

            reset_button = pygame.Rect((WIDTH - BUTTON_WIDTH) / 2 - 200, CELL_DIM * 9 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
            restart_button = pygame.Rect((WIDTH - BUTTON_WIDTH) / 2, CELL_DIM * 9 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
            exit_button = pygame.Rect((WIDTH - BUTTON_WIDTH) / 2 + 200, CELL_DIM * 9 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
          
            # the 3 game option buttons
            # color of buttons
            pygame.draw.rect(screen, BUTTON_COLOR, reset_button)
            pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)

            # border of buttons
            pygame.draw.rect(screen, TEXT_COLOR, reset_button, 2)
            pygame.draw.rect(screen, TEXT_COLOR, restart_button, 2)
            pygame.draw.rect(screen, TEXT_COLOR, exit_button, 2)

            # inserts text on buttons
            screen.blit(reset_option, ((WIDTH - reset_option.get_rect().width) / 2 - 200, (CELL_DIM * 9 + BUTTON_HEIGHT / 2)))
            screen.blit(restart_option, ((WIDTH - restart_option.get_rect().width) / 2, (CELL_DIM * 9 + BUTTON_HEIGHT / 2)))
            screen.blit(exit_option, ((WIDTH - exit_option.get_rect().width) / 2 + 200, (CELL_DIM * 9 + BUTTON_HEIGHT / 2)))

        # game over screen
        if screen_type == 'lose_screen':  
            game_over = title_font.render("GAME OVER", True, TEXT_COLOR)
            screen.blit(game_over, ((WIDTH - game_over.get_rect().width) / 2, 100))

            # creates button
            restart_button = pygame.Rect((WIDTH - BUTTON_WIDTH) / 2, HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)

            # draws button and border
            pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
            pygame.draw.rect(screen, TEXT_COLOR, restart_button, 2)

            # inserts text on buttons
            screen.blit(restart_option, ((WIDTH/2 - BUTTON_WIDTH/3, HEIGHT/2 + BUTTON_HEIGHT/4)))

        # game won screen
        if screen_type == 'win_screen':  
            game_won = title_font.render("GAME WON!", True, TEXT_COLOR)
            screen.blit(game_won, ((WIDTH - game_won.get_rect().width) / 2, 100))

            # creates button
            exit_button = pygame.Rect((WIDTH - BUTTON_WIDTH) / 2, HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)

            # draws button and border
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
            pygame.draw.rect(screen, TEXT_COLOR, exit_button, 2)

            # inserts text on buttons
            screen.blit(exit_option, ((WIDTH/2 - BUTTON_WIDTH/5, HEIGHT/2 + BUTTON_HEIGHT/4)))

      # updates game display
        pygame.display.update()


if __name__ == '__main__':
    main()
