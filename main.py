import time
import os
import platform
import _thread as thread
import msvcrt

board =[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,-1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

pos = [2,7]
score = 3
direct = "up"

runn = True
def chgDirect(pa1,pa2):
    global runn, direct
    while runn:
        key = ord(msvcrt.getch())
        if (key == 3): # Ctrl C
            print("Die")
            runn = False
        elif key == 0:
            key = ord(msvcrt.getch())
            if key == 80:
                direct = "down"
            elif key == 72:
                direct = "up"
            elif key == 75:
                direct = "left"
            elif key == 77:
                direct = "right"
            else:
                print(key)
        else:
            print(key)

def foodDrop(pa1,pa2):
    global board
    

try:
    thread.start_new_thread( chgDirect , ('',''))
    thread.start_new_thread( foodDrop , ('',''))
    while runn:
        if board[pos[0]][pos[1]] == -1:
            score += 1
        board[pos[0]][pos[1]] = score
        # Render
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not type(board[i][j]) == str:
                    if board[i][j] > 0:
                        board[i][j] -= 1
                        print("█", end='')
                    elif board[i][j] == 0:
                        print("░", end='')
                    elif board[i][j] == -1:
                        print("®", end='')
            print("")
        time.sleep(.3) # Wait then clear
        if platform.system() == 'Windows':
            os.system('cls')  # For Windows
        if platform.system() == 'Linux':
            os.system('clear')  # For Linux/OS X

        # Move
        if direct == "up":
            pos[0] -=1
        elif direct == "down":
            pos[0] +=1
        elif direct == "left":
            pos[1] -=1
        elif direct == "right":
            pos[1] +=1
except KeyboardInterrupt:
    print("Bye")