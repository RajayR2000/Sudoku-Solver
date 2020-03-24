import pygame
import time
from sudoku_solver import solve_board


pygame.init()
win = pygame.display.set_mode((630, 630))
win.fill((255, 255, 255))
sol=[[0 for i in range(9)]for j in range(9)]

class Board:
    board=[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.cubes=[[Cube(i,j,self.board[i][j]) for j in range(9)]for i in range(9)]

    def draw_board(self):
        gap = 630 / 9
        for i in range(10):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1

            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (630, i * gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, 630), thick)

        for i in range(9):
            for j in range(9):
                self.cubes[i][j].draw_cube(self.board)

        pygame.display.update()

    def display_solution(self):
        solve_board(self.board)

class Cube:
    def __init__(self,x,y,val):
        self.x=x
        self.y=y
        self.val=val

    def draw_cube(self,board):
        gap=630/9
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render(str(board[self.x][self.y]), 1, (128, 128, 128))
        win.blit(text, (gap*self.x+9, gap*self.y+9))




def redraw_window(win,board_obj):
    win.fill((255, 255, 255))
    board_obj.draw_board()


def start_game():
    board_obj=Board(630,630)
    playing=True
    while playing:
        redraw_window(win,board_obj)
        pygame.time.delay(1000)
        solve_board(board_obj.board)
        print_board(board_obj.board)
        redraw_window(win,board_obj)
        print_board(board_obj.board)
        pygame.time.delay(1000)
        break

def print_board(board):
    for i in range(9):
        if(i%3 == 0 and i!=0):
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if(j%3 == 0 and j!=0):
                print(" | ", end="")

            if(j==8):
                print(board[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
start_game()



