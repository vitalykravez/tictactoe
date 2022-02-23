import random
import sys
import time
from turtle import right

import pygame as pg
from pygame.locals import *


# Init global varisables
APP_NAME = "Tic Tac Toe"
XO = "x"
WINNER = None
DRAW = False
WIDTH = 400
HEIGHT = 400
WHITE = (255, 255, 255)
LINE_COLOR = (10, 10, 10)
CHOICES = [val for val in range(1, 10)]
HISTORY_LIST = []
FINISHED = False
FPS = 30

# TTT 3x3 board
TTT = [[None] * 3, [None] * 3, [None] * 3]


def draw_status():
    """Black rectangle with game info"""

    global DRAW

    if WINNER is None:
        message = XO.upper() + "'s Turn"
    else:
        message = WINNER.upper() + " won!"
    if DRAW:
        message = "Draw!"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # Copy the rendered message onto the board
    screen.fill((0, 0, 0), (0, 400, 500, 200))
    text_rect = text.get_rect(center=(WIDTH / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()


def game_opening():
    """Starting window and gamefield init"""

    screen.blit(opening, (0, 100))
    pg.display.update()
    time.sleep(1)
    screen.fill(WHITE)

    # Drawing vertical lines
    pg.draw.line(screen, LINE_COLOR, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pg.draw.line(
        screen, LINE_COLOR, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7
    )
    # Drawing horizontal lines
    pg.draw.line(screen, LINE_COLOR, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
    pg.draw.line(
        screen, LINE_COLOR, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7
    )
    draw_status()


def check_win():
    """Every turn winning check"""

    global TTT, WINNER, DRAW

    # Check for winning rows
    for row in range(0, 3):
        if (TTT[row][0] == TTT[row][1] == TTT[row][2]) and (
            TTT[row][0]
        ) is not None:
            # this row won
            WINNER = TTT[row][0]
            pg.draw.line(
                screen,
                (0, 0, 0),
                (0, (row + 1) * HEIGHT / 3 - HEIGHT / 6),
                (WIDTH, (row + 1) * HEIGHT / 3 - HEIGHT / 6),
                10,
            )
            break
    # Check for winning columns
    for col in range(0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (
            TTT[0][col]
        ) is not None:
            # this column won
            WINNER = TTT[0][col]
            pg.draw.line(
                screen,
                (0, 0, 0),
                ((col + 1) * WIDTH / 3 - WIDTH / 6, 0),
                ((col + 1) * WIDTH / 3 - WIDTH / 6, HEIGHT),
                10,
            )
            break
    # Check diagonal winner
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        # won diagonally left to right
        WINNER = TTT[0][0]
        pg.draw.line(screen, (0, 0, 0), (50, 50), (350, 350), 10)
    # Check diagonal winner
    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
        # won diagonally right to left
        WINNER = TTT[0][2]
        pg.draw.line(screen, (0, 0, 0), (350, 50), (50, 350), 10)
    if all([all(row) for row in TTT]) and WINNER is None:
        DRAW = True
    draw_status()


def drawXO(row, col):
    """Every turn X or O draw"""

    global TTT, XO

    if row == 1:
        posx = 30
    if row == 2:
        posx = WIDTH / 3 + 30
    if row == 3:
        posx = WIDTH / 3 * 2 + 30
    if col == 1:
        posy = 30
    if col == 2:
        posy = HEIGHT / 3 + 30
    if col == 3:
        posy = HEIGHT / 3 * 2 + 30
    TTT[row - 1][col - 1] = XO
    if XO == "x":
        screen.blit(x_img, (posy, posx))
        XO = "o"
    else:
        screen.blit(o_img, (posy, posx))
        XO = "x"
    pg.display.update()


def randomAI():
    """Random bot interface"""

    choice = CHOICES.pop(CHOICES.index(random.choice(CHOICES)))
    if choice in range(1, 4):
        row = 1
        col = choice
    if choice in range(4, 7):
        row = 2
        col = choice - 3
    if choice in range(7, 10):
        row = 3
        col = choice - 6
    return row, col


def AIgame():
    """AI game against eachother"""

    row, col = randomAI()

    if row and col and TTT[row - 1][col - 1] is None:
        global XO

        # save history
        HISTORY_LIST.append([row, col, XO])

        # draw the x or o on screen
        drawXO(row, col)
        check_win()


def draw_history():
    """Draw a history at the end of game"""

    global DRAW, HISTORY_LIST

    message = "Game turns history:"

    font = pg.font.Font(None, 20)
    text = font.render(message, 1, (255, 255, 255))

    # Copy the rendered message onto the board
    # screen.fill((0,0,0), (0,400,500,200))
    text_rect = text.get_rect(center=(WIDTH / 2, 500 - 30))
    screen.blit(text, text_rect)

    for i in range(len(HISTORY_LIST)):
        turn = HISTORY_LIST[i]
        message = f"{i+1} turn: {turn[2]}[{str(turn[0])}][{str(turn[1])}]"
        font = pg.font.Font(None, 16)
        text = font.render(message, 1, (255, 255, 255))

        # screen.fill((0,0,0), (0,400,500,200))
        text_rect = text.get_rect(center=(WIDTH / 2, 535 + 13 * (i - 4)))
        screen.blit(text, text_rect)
    pg.display.update()


# Init pygame window
pg.init()
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT + 200), 0, 32)
pg.display.set_caption(APP_NAME)

# Loading the images
opening = pg.image.load(".\images\mainttt.png")
x_img = pg.image.load(".\images\X.png")
o_img = pg.image.load(".\images\O.png")

# resizing images
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening, (WIDTH, HEIGHT))


if __name__ == "__main__":
    game_opening()

    # Run the game loop forever
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and not FINISHED:
                    if WINNER or DRAW:
                        draw_history()
                        FINISHED = True
                        time.sleep(1)
                    else:
                        AIgame()
                elif event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
        pg.display.update()
        CLOCK.tick(FPS)
