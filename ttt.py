
from turtle import right
import pygame as pg, sys
from pygame.locals import *
import random
import time


# Init global varisables
app_name = "Tic Tac Toe"
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)
choices = [val for val in range(1, 10)]
history_list = []
finished = False

# TTT 3x3 board
TTT = [[None]*3, [None]*3, [None]*3]

# Init pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+200), 0, 32)
pg.display.set_caption(app_name)

# Loading the images
opening = pg.image.load('.\images\mainttt.png')
x_img = pg.image.load('.\images\X.png')
o_img = pg.image.load('.\images\O.png')

# resizing images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height))


def draw_status():
    """Black rectangle with game info"""
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Draw!"
    
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255,255,255))

    # Copy the rendered message onto the board
    screen.fill((0,0,0), (0,400,500,200))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def game_opening():
    screen.blit(opening,(0,100))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    
    # Drawing vertical lines
    pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
    draw_status()
    

def check_win():
    global TTT, winner, draw

    # Check for winning rows
    for row in range(0,3):
        if ((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0]) is not None):
            # this row won
            winner = TTT[row][0]
            pg.draw.line(screen, (0,0,0), (0, (row+1)*height/3-height/6), (width, (row+1)*height/3 - height/6), 10)
            break

    # Check for winning columns
    for col in range(0,3):
        if ((TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col]) is not None):
            # this column won
            winner = TTT[0][col]
            pg.draw.line(screen, (0,0,0), ((col+1)*width/3-width/6, 0), ((col+1)*width/3-width/6, height), 10)
            break
    
    # Check diagonal winner
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        # won diagonally left to right
        winner = TTT[0][0]
        pg.draw.line(screen, (0,0,0), (50,50), (350,350), 10)

    # Check diagonal winner
    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
        # won diagonally right to left
        winner = TTT[0][2]
        pg.draw.line(screen, (0,0,0), (350,50), (50,350), 10)
    
    if (all([all(row) for row in TTT]) and winner is None):
        draw = True
    draw_status()

def drawXO(row,col):
    global TTT, XO

    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width/3*2 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height/3*2 + 30
    
    TTT[row-1][col-1] = XO
    if (XO == 'x'):
        screen.blit(x_img, (posy,posx))
        XO = 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO = 'x'
    pg.display.update()

def randomAI():
    """Random bot interface"""
    choice = choices.pop(choices.index(random.choice(choices)))
    if choice in range(1,4):
        row = 1
        col = choice
    if choice in range(4,7):
        row = 2
        col = choice - 3
    if choice in range(7,10):
        row = 3
        col = choice - 6

    return row, col

# def x_intelligentAI():
#     """X-master interface"""

   



#     return row, col

def AIgame():
    """AI game against eachother"""
    
    # "X"-master against "O"-random
    # if len(choices) % 2 == 1:
    #     row, col = x_intelligentAI()
    # else:
    #     row, col = randomAI()
    # Random choice of remaining slot on each turn
    row, col = randomAI()

    if (row and col and TTT[row-1][col-1] is None):
        global XO
        
        # save history
        history_list.append([row, col, XO])

        # draw the x or o on screen
        drawXO(row,col)
        check_win()
        

def draw_history():
    global draw, history_list

    message = "Game turns history:"
    
    font = pg.font.Font(None, 20)
    text = font.render(message, 1, (255,255,255))

    # Copy the rendered message onto the board
    # screen.fill((0,0,0), (0,400,500,200))
    text_rect = text.get_rect(center=(width/2, 500-30))
    screen.blit(text, text_rect)

    for i in range(len(history_list)):
        turn = history_list[i]
        message = f"{i+1} turn: {turn[2]}[{str(turn[0])}][{str(turn[1])}]"
        font = pg.font.Font(None, 16)
        text = font.render(message, 1, (255,255,255))

        # screen.fill((0,0,0), (0,400,500,200))
        text_rect = text.get_rect(center=(width/2, 535+13*(i-4)))
        screen.blit(text, text_rect)
    
    pg.display.update()


if __name__ == "__main__":
    game_opening()

    # Run the game loop forever
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and not finished:
                    if (winner or draw):
                        draw_history()
                        finished = True
                        time.sleep(1)                
                    else:
                        AIgame()
                elif event.key == K_ESCAPE:
                        pg.quit()
                        sys.exit()
        
        pg.display.update()
        CLOCK.tick(fps)