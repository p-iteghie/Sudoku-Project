import sys
import sudoku_generator as sg
from cell import Cell
from board import Board
import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    title_font = pygame.font.Font("Luciole-Bold.ttf", 45)
    select_font = pygame.font.Font("Luciole-Regular.ttf", 35)
    mode_font = pygame.font.Font("Luciole-Bold.ttf", 25)
    option_font = pygame.font.Font("Luciole-Bold.ttf", 25)

    title = title_font.render("Welcome to Sudoku!", True, TEXT_COLOR)
    select = select_font.render("Select a Game Mode:", True, TEXT_COLOR)
    easy_mode = mode_font.render("EASY", True, BG_COLOR)
    medium_mode = mode_font.render("MEDIUM", True, BG_COLOR)
    hard_mode = mode_font.render("HARD", True, BG_COLOR)

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

    reset_option = option_font.render("RESET", True, BG_COLOR)
    restart_option = option_font.render("RESTART", True, BG_COLOR)
    exit_option = option_font.render("EXIT", True, BG_COLOR)

    reset_button = pygame.Rect(15, CELL_DIM * 9 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    restart_button = pygame.Rect(225, CELL_DIM * 9 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    exit_button = pygame.Rect(435, CELL_DIM * 9 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)

    screen_type = 'welcome_screen'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_type == 'welcome_screen':
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
                elif screen_type == 'play_game':
                    if reset_button.collidepoint(event.pos):  # clears the board
                        for box in board.cell_list:
                            box.sketch = ""
                            # add code to clear submitted guesses or reset somehow
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
                                    # submitting a guess


        screen.fill(BG_COLOR)

        if screen_type == 'welcome_screen':
            screen.blit(title, ((WIDTH - title.get_rect().width) / 2, 100))
            screen.blit(select, ((WIDTH - select.get_rect().width) / 2, 350))

            for button in mode_buttons_border:
                pygame.draw.rect(screen, TEXT_COLOR, button)

            pygame.draw.rect(screen, BUTTON_COLOR, easy_button)
            pygame.draw.rect(screen, BUTTON_COLOR, medium_button)
            pygame.draw.rect(screen, BUTTON_COLOR, hard_button)

            screen.blit(easy_mode, (
                (WIDTH - easy_mode.get_rect().width) / 2, 400 + (BUTTON_HEIGHT - easy_mode.get_rect().height) / 2))
            screen.blit(medium_mode, ((WIDTH - medium_mode.get_rect().width) / 2,
                                      400 + BUTTON_HEIGHT + 20 + (BUTTON_HEIGHT - easy_mode.get_rect().height) / 2))
            screen.blit(hard_mode, ((WIDTH - hard_mode.get_rect().width) / 2,
                                    400 + (BUTTON_HEIGHT + 20) * 2 + (BUTTON_HEIGHT - easy_mode.get_rect().height) / 2))

        if screen_type == 'play_game':
            board.draw()

            # the 3 game option buttons
            # color of buttons
            pygame.draw.rect(screen, BUTTON_COLOR, reset_button)
            pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)

            # border of buttons
            pygame.draw.rect(screen, TEXT_COLOR, reset_button, 2)
            pygame.draw.rect(screen, TEXT_COLOR, restart_button, 2)
            pygame.draw.rect(screen, TEXT_COLOR, exit_button, 2)

            # text on buttons
            screen.blit(reset_option, ((BUTTON_WIDTH / 2 - 20), (CELL_DIM * 9 + BUTTON_HEIGHT / 2)))
            screen.blit(restart_option, ((BUTTON_WIDTH / 2 + 170), (CELL_DIM * 9 + BUTTON_HEIGHT / 2)))
            screen.blit(exit_option, ((BUTTON_WIDTH / 2 + 400), (CELL_DIM * 9 + BUTTON_HEIGHT / 2)))

        pygame.display.update()


if __name__ == '__main__':
    main()

'''
bens mistake ignore this pls (he doesn't want to delete his embarrasment -pat)(i put too much work i cant just delete it... -ben)
print('---------------------------') 
i=0
while i<9:
  j=0
  while j<3:
    k = i % 3

    print(hi[j][(3*k):(3*(k+1))], end ='')
    j+=1
  print('\n---------------------------') if i%3 == 2 else print()
  i += 1
'''
