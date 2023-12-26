#!/usr/bin/env python
# coding: utf-8

# In[89]:


"""Human vs. Human Tic-Tac-Toe"""
import random

rows = 3
collums = 3

lettersCol = ["A", "B", "C"]
gameBoard = [["", "", ""], ["", "", ""], ["", "", ""]]

def board():
    print("    A   B   C ", end = " ")
    for i in range(rows):
        print("\n --------------")
        print(i, "|", end = "")
        for j in range(collums):
            if gameBoard[i][j] == "X":
                print("", gameBoard[i][j], end  = " |")
            elif gameBoard[i][j] == "O":
                print("", gameBoard[i][j], end  = " |")
            else:
                print(" ", gameBoard[i][j], end  = " |")
    print("\n --------------")     
    
def modBoard(pick, turn):
    gameBoard[pick[0]][pick[1]] = turn
    
def winnerCheck(coins):
    for j in range(rows):
        i = 0
        if gameBoard[i][j] == coins and gameBoard[i+1][j] == coins and gameBoard[i+2][j]:
            print(coins, "wins! Congratulations! Here's the final Game Board! \n")
            return True

    for i in range(rows):
        j = 0
        if gameBoard[i][j] == coins and gameBoard[i][j+1] == coins and gameBoard[i][j+2] == coins:
            print(coins, "wins! Congratulations! Here's the final Game Board! \n")
            return True
            
    for i in range(rows - 2):
        for j in range(2, collums):
            if gameBoard[i][j] == coins and gameBoard[i+1][j-1] == coins and gameBoard[i+2][j-2] == coins:
                print(coins, "wins! Congratulations! Here's the final Game Board! \n")
                return True
            
    for i in range(rows - 2):
        for j in range(collums - 2):
            if gameBoard[i][j] == coins and gameBoard[i+1][j+1] == coins and gameBoard[i+2][j+2] == coins:
                print("\n", coins, "wins! Congratulations! Here's the final Game Board!")
                return True
    return False

def coordinates(inputCoor):
    coor = [[ ],[ ]]
    if inputCoor[0] == "A":
        coor[1] = 0
    elif inputCoor[0] == "B":
        coor[1] = 1
    elif inputCoor[0] == "C":
        coor[1] = 2
    else:
        print("Enter a new valid cooridnate!")
    coor[0] = int(inputCoor[1])
    return coor

def validSpace(guessCoor):
    if gameBoard[guessCoor[0]][guessCoor[1]] == "O":
        return False
    elif gameBoard[guessCoor[0]][guessCoor[1]] == "X":
        return False
    else:
        return True

turns = 0
winner = False
    
while winner == False:
    if turns % 2 == 0:
        board()
        while True:
            pick = input("\n Player X pick a spot to drop your chip: ")
            coordinate = coordinates(pick)
            
            if validSpace(coordinate):
                modBoard(coordinate, "X")
                break
            else:
                print("Enter a different valid coordinate!")
                
        win = winnerCheck("X")
        turns = turns + 1
        
    else:
        while True:
            pick = input("\n Player O pick a spot to drop your chip: ")
            coordinate = coordinates(pick)
            
            if validSpace(coordinate):
                modBoard(coordinate, "O")
                break
            else:
                print("Enter a different valid coordinate!")
                
        win = winnerCheck("O")
        turns = turns + 1
    
    if(win):
        board()
        break


# In[86]:


"""Human vs. Computer Tic-Tac-Toe"""
import random

rows = 3
collums = 3

lettersCol = ["A", "B", "C"]
gameBoard = [["", "", ""], ["", "", ""], ["", "", ""]]

def board():
    print("    A   B   C ", end = " ")
    for i in range(rows):
        print("\n --------------")
        print(i, "|", end = "")
        for j in range(collums):
            if gameBoard[i][j] == "X":
                print("", gameBoard[i][j], end  = " |")
            elif gameBoard[i][j] == "O":
                print("", gameBoard[i][j], end  = " |")
            else:
                print(" ", gameBoard[i][j], end  = " |")
    print("\n --------------")     
    
def modBoard(pick, turn):
    gameBoard[pick[0]][pick[1]] = turn
    
def winnerCheck(coins):
    for j in range(rows):
        i = 0
        if gameBoard[i][j] == coins and gameBoard[i+1][j] == coins and gameBoard[i+2][j]:
            print(coins, "wins! Congratulations! Here's the final Game Board! \n")
            return True

    for i in range(rows):
        j = 0
        if gameBoard[i][j] == coins and gameBoard[i][j+1] == coins and gameBoard[i][j+2] == coins:
            print(coins, "wins! Congratulations! Here's the final Game Board! \n")
            return True
            
    for i in range(rows - 2):
        for j in range(2, collums):
            if gameBoard[i][j] == coins and gameBoard[i+1][j-1] == coins and gameBoard[i+2][j-2] == coins:
                print(coins, "wins! Congratulations! Here's the final Game Board! \n")
                return True
            
    for i in range(rows - 2):
        for j in range(collums - 2):
            if gameBoard[i][j] == coins and gameBoard[i+1][j+1] == coins and gameBoard[i+2][j+2] == coins:
                print("\n", coins, "wins! Congratulations! Here's the final Game Board!")
                return True
    return False

def coordinates(inputCoor):
    coor = [[ ],[ ]]
    if inputCoor[0] == "A":
        coor[1] = 0
    elif inputCoor[0] == "B":
        coor[1] = 1
    elif inputCoor[0] == "C":
        coor[1] = 2
    else:
        print("Enter a new valid cooridnate!")
    coor[0] = int(inputCoor[1])
    return coor

def validSpace(guessCoor):
    if gameBoard[guessCoor[0]][guessCoor[1]] == "O":
        return False
    elif gameBoard[guessCoor[0]][guessCoor[1]] == "X":
        return False
    else:
        return True

turns = 0
winner = False
    
while winner == False:
    if turns % 2 == 0:
        board()
        while True:
            pick = input("\nPick a spot to drop your chip: ")
            coordinate = coordinates(pick)
            
            if validSpace(coordinate):
                modBoard(coordinate, "X")
                break
            else:
                print("Enter a different valid coordinate!")
                
        win = winnerCheck("X")
        turns = turns + 1
        
    else:
        while True:
            computerPick = [random.choice(lettersCol), random.randint(0,2)]
            computerCoor = coordinates(computerPick)
            if validSpace(computerCoor):
                modBoard(computerCoor, "O")
                break
                
        win = winnerCheck("O")
        turns = turns + 1
    
    if(win):
        board()
        break


# In[109]:


"""Computer vs. Computer Tic-Tac-Toe"""
import random

rows = 3
collums = 3

lettersCol = ["A", "B", "C"]
gameBoard = [["", "", ""], ["", "", ""], ["", "", ""]]

def board():
    print("    A   B   C ", end = " ")
    for i in range(rows):
        print("\n --------------")
        print(i, "|", end = "")
        for j in range(collums):
            if gameBoard[i][j] == "X":
                print("", gameBoard[i][j], end  = " |")
            elif gameBoard[i][j] == "O":
                print("", gameBoard[i][j], end  = " |")
            else:
                print(" ", gameBoard[i][j], end  = " |")
    print("\n --------------")     
    
def modBoard(pick, turn):
    gameBoard[pick[0]][pick[1]] = turn
    
def winnerCheck(coins):
    for j in range(rows):
        i = 0
        if gameBoard[i][j] == coins and gameBoard[i+1][j] == coins and gameBoard[i+2][j]:
            print(coins, "wins! Congratulations! Here's the final Game Board! \n")
            return True

    for i in range(rows):
        j = 0
        if gameBoard[i][j] == coins and gameBoard[i][j+1] == coins and gameBoard[i][j+2] == coins:
            print(coins, "wins! Congratulations! Here's the final Game Board! \n")
            return True
            
    for i in range(rows - 2):
        for j in range(2, collums):
            if gameBoard[i][j] == coins and gameBoard[i+1][j-1] == coins and gameBoard[i+2][j-2] == coins:
                print(coins, "wins! Congratulations! Here's the final Game Board! \n")
                return True
            
    for i in range(rows - 2):
        for j in range(collums - 2):
            if gameBoard[i][j] == coins and gameBoard[i+1][j+1] == coins and gameBoard[i+2][j+2] == coins:
                print("\n", coins, "wins! Congratulations! Here's the final Game Board!")
                return True
    return False

def coordinates(inputCoor):
    coor = [[ ],[ ]]
    if inputCoor[0] == "A":
        coor[1] = 0
    elif inputCoor[0] == "B":
        coor[1] = 1
    elif inputCoor[0] == "C":
        coor[1] = 2
    else:
        print("Enter a new valid cooridnate!")
    coor[0] = int(inputCoor[1])
    return coor

def validSpace(guessCoor):
    if gameBoard[guessCoor[0]][guessCoor[1]] == "O":
        return False
    elif gameBoard[guessCoor[0]][guessCoor[1]] == "X":
        return False
    else:
        return True

turns = 0
winner = False
    
while winner == False:
    if turns % 2 == 0:
        board()
        while True:
            computerPick = [random.choice(lettersCol), random.randint(0,2)]
            computerCoor = coordinates(computerPick)
            if validSpace(computerCoor):
                modBoard(computerCoor, "X")
                break
        win = winnerCheck("X")
        turns = turns + 1
        
    else:
        while True:
            computerPick = [random.choice(lettersCol), random.randint(0,2)]
            computerCoor = coordinates(computerPick)
            if validSpace(computerCoor):
                modBoard(computerCoor, "O")
                break
                
        win = winnerCheck("O")
        turns = turns + 1
    
    if(win):
        board()
        break

