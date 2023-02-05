import numpy as np
import sys
import math
import pygame


blue= (0,0,255)
black=(0,0,0)
red=(255,0,0)

row_count=6
column_count=7

def create_board():
    board=np.zeros((row_count,column_count))
    return board

def drop_piece(board,row,col,piece):
    board[row][col]= piece

def is_valid(board,col):
    return board[row_count-1][col]==0

def get_next_open_row(board,col):
    for r in range(row_count):
        if board[r][col]==0:
            return r

def print_board(board):
    print(np.flip(board,0))


def game_draw(board,piece1,piece2):
    draw=0
    for r in range(0,row_count-1):     
         for c in range(0,column_count):
          
            if (board[r][c]==piece1 or board[r][c]==piece2) and (board[r][c-1]==piece1 or board[r][c-1]==piece2) and (board[r][c-2]==piece1 or board[r][c-2]==piece2) and (board[r][c-3]==piece1 or board[r][c-3]==piece2) and (board[r][c-4]==piece1 or board[r][c-4]==piece2) and (board[r][c-5]==piece1 or board[r][c-5]==piece2) and (board[r][c-6]==piece1 or board[r][c-6]==piece2) and (board[r][c-7]==piece1 or board[r][c-7]==piece2):
                draw=0
            else:
                draw=1
    if draw==0:
        return True
    else:
        return False


def winning_move(board,piece):
    #checking horizontal positions
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c]==piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    #checking vertical positions
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    
    #checking positively sloped positions
    for c in range(column_count-3):
        for r in range(row_count-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    #checking negatively sloped diagonals
    for c in range(column_count-3):
        for r in range(3,row_count):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True   

def draw_board(board):
    for c in range(column_count):
        for r in range(row_count-1):
             pygame.draw.rect(screen,(127, 214, 117, 1), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
             pygame.draw.circle(screen,black, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(column_count):
        for r in range(row_count-1):
            if board[r][c]==1:
                pygame.draw.circle(screen, red, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c]==2:
                pygame.draw.circle(screen,blue, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()        




                

 


#initialize the board
board=create_board()
print_board(board)

turn=0

#initialize the game
pygame.init()

#define the screen size
SQUARESIZE=100

#define width and height of board
width=column_count * SQUARESIZE
height=row_count* SQUARESIZE

size=(width,height)

RADIUS=int(SQUARESIZE/2 - 5)

screen=pygame.display.set_mode(size)




#Calling function draw_board again

pygame.display.update()
pygame.display.set_caption("CONNECT 4")
icon=pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)


def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
            mouse=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()

            #button display
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(screen,ac,(x,y,w,h))
                if click[0]==1 and action!=None:
                    action()
                    
            else:
                pygame.draw.rect(screen,ic,(x,y,w,h))
            
            
            #button texts
            smallText=pygame.font.Font("freesansbold.ttf",20)
            textSurf,textRect=text_objects(msg,smallText)
            textRect.center=(x+(w/2),y+(h/2))
            screen.blit(textSurf,textRect)
            

def quitGame():
    pygame.quit()
    quit()

def game_play():
  

  
  turn=0
  draw_board(board)
 
  
  pygame.display.update()

  myFont=pygame.font.SysFont("Lucida Fax",75)

  game_over=False
  while not game_over:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,black,(0,0,width,SQUARESIZE))
            posx=event.pos[0]
            if turn==0:
                pygame.draw.circle(screen,red,(posx,int(SQUARESIZE/2)),RADIUS)
            else:
                pygame.draw.circle(screen,blue,(posx,int(SQUARESIZE/2)),RADIUS)
        pygame.display.update()

        if event.type==pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,black,(0,0,width,SQUARESIZE))
            
            #ASk for player 1 input
            if turn==0:
                posx=event.pos[0]
                col=int(math.floor(posx/SQUARESIZE))

                if is_valid(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board,1):
                       label=myFont.render("Player 1 WINS!!",1,red)
                       screen.blit(label,(40,10))
                       game_over=True 
                    
                    elif game_draw(board,1,2):
                        label=myFont.render("GAME DRAW",1,red)
                        screen.blit(label,(40,10))
                        game_over=True 


                    

            #ask for player 2 input
            else:
                posx=event.pos[0]
                col=int(math.floor(posx/SQUARESIZE))
                
                if is_valid(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,row,col,2)

                    if winning_move(board,2):
                        label=myFont.render("Player 2 wins!!",1,blue)
                        screen.blit(label,(40,10))
                        game_over=True

                    elif game_draw(board,1,2):
                        label=myFont.render("GAME DRAW",1,red)
                        screen.blit(label,(70,10))
                        game_over=True 
            print_board(board)
            draw_board(board)

            turn+=1
            turn=turn%2

            if game_over:
                pygame.time.wait(3000)
                
        
def start_menu():
     intro=True

     while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      
           
            
        bg=pygame.image.load('bg3.jpeg')  
        bgx=0
        bgy=0
            
            
        largeText = pygame.font.SysFont("Broadway",115)
        TextSurf, TextRect = text_objects("CONNECT 4", largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf, TextRect)
            
            
        myFont=pygame.font.SysFont("Lucida Fax",80)
        screen.blit(bg,(bgx,bgy))
        label=myFont.render("CONNECT 4",1,(77,154,230))
        screen.blit(label,(width/6,10))
            
            
        button("START GAME",260,150,width/5,SQUARESIZE/2,(162,219,252,255),(96,167,221,255),game_play)
        button("QUIT",260,220,width/5,SQUARESIZE/2,(162,219,252,255),(96,167,221,255),quitGame)
        pygame.display.update()
            
            
start_menu()



"""player1=input('Enter name of player 1')
player2=input('Enter name of player 2')

while not game_over:
    #ask player 1 for input
    if turn==0:
        col=int(input(f"{player1},select a column between 0-{row_count}"))
        if is_valid(board,col):
            row=get_next_open_row(board,col)
            drop_piece(board,row,col,1)

    else:
        col=int(input(f"{player2},select a column between 0-{row_count}"))
        if is_valid(board,col):
            row=get_next_open_row(board,col)
            drop_piece(board,row,col,2)
    print_board(board)
    turn+=1
    turn=turn%2"""

