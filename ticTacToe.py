#!/usr/bin/env python
# coding: utf-8

# In[11]:


#3x3 grid
#3 in a row ([x][x+1]), col ([x+1][x]), dia ([x+1][x+-1]= WIN CON
#Check win con every loop
#Fill boxes with either "X" or "O"
#If grid is filled with win con not met = DRAW
import math


# In[12]:


def createNewGrid():
    grid=[[float("nan") for i in range(3)] for i in range(3)]
    return grid


# In[13]:


#Set as 1 and 4 so that no matter which case 
#player_X = 1
#player_O = 4

#whoWon = False


# In[14]:


#testForRow = [[1,1,1],[4,4,4],[5,5,5]]
#testForCol = [[1,4,15],[1,4,15],[1,4,15]]
#testForDiag = [[1,13,4],[13,4,13],[4,13,1]]


# In[15]:


#Win Condition - Rows
#Checks the sum of each array to determine whether a win condion is met for X or O
def rowWinCon():
    for row in testForRow:
        print(row)
        if sum(row) == 3 * player_X:
            print("X's have won")
            whoWon = player_X
            isgameOver = True

        elif sum(row) == 3 * player_O:
            print("O's have won")
            whoWon = player_O
            isgameOver = True

        else:
            print("Draw")
            whowon = False
            


# In[16]:


#Win Condition - Columns
def colWinCon():
    for col in range(3):
        total = 0
        print("Col: ", col)
        for row in range(3):
            print("Row: ", row)
            total += testForCol[row][col]
            print("Total: ", total)
        #Check if the win con is met    
        if total == 3 * player_X:
            print("X's have won")
            whoWon = player_X
            isgameOver = True
            
        elif total == 3 * player_O:
            print("O's have won")
            whoWon = player_O
            isgameOver = True
            
        else:
            print("Draw")
            whoWon = False



# In[17]:


# define column sum
# define diag sum

# board[00]


# In[18]:


### check rows sum is 12 or 3
### check cols sum  sum(test)
### check diag sum


### then check for draw

### else next turn


# In[19]:


#Win Condion - Diagionals
# Either ([0][0],[1][1],[2][2]) or ([2][2],[1][1],[0][0])
#diagTlBrTotal is  from Top Left to Bottom Right
#diagTrBLTotal is from Top Right to Bottom Left
def diagWinCon():
    diagTlBrTotal = 0
    diagTrBlTotal = 0
    for col in range(3):
        #print("Col: ", col)
        for row in range(3):
            #print("Row: ", row)
            if row == col:
                diagTlBrTotal += testForDiag[row][col]
                diagTrBlTotal += testForDiag[row][2-col]

            #elif row == 2-col:
                #print(row, col)
                #inverseTotal += testForDiag[row][3-col]
            print("Total: ", diagTlBrTotal)
            print("Inverse: ",diagTrBlTotal)
    print("Final Total: ", diagTlBrTotal)
    print("Final Inverse Total: ", diagTrBlTotal)

    #Conditions for game state
    if diagTlBrTotal == 3 * player_X or diagTrBlTotal == 3 * player_X:
        print("X's have won")
        whoWon = player_X
        isgameOver = True

    elif diagTlBrTotal == 3 * player_X or diagTrBlTotal == 3 * player_O:
        print("O's have won")
        whoWon = player_O
        isgameOver = True

    else:
        print("Draw")
        whoWon = False
    


# In[20]:


#Draw condition
def drawCon():
    for row in grid:
        for value in row:
            print(value)
            if math.isnan(value) == True:
                isGameOver = False
                break
            else:
                isGameOver = True
    
    print(isGameOver)



# In[21]:


def playerMove(playerTurn):
    while True:
        #Asks user for input to find out what row they want to interact with
        makeMoveRow = int(input("What row do+ you want to put your symbol in?: 1, 2, 3 "))

        #Asks user for input to find out what column they want to interact with
        makeMoveCol = int(input("What column do you want to put the symbol in?: 1, 2, 3 "))

        #Postion the user whants to replace the value of in the grid
        valueToReplace = grid[makeMoveRow-1][makeMoveCol-1] 
        print(valueToReplace)

        #Action to replace value user want to either "X" or "O"
        if math.isnan(valueToReplace) == True: 
            grid[makeMoveRow-1][makeMoveCol-1] = playerTurn
            print(grid)
            break
        else:
            print("This spot has already been taken")



# In[31]:


def playTicTacToe():
    #Declaring variables
    player_X = 1
    player_O = 4
    whoWon = False
    isgameOver = False
    playerTurns = [player_X, player_O, player_X, player_O, player_X, player_O, player_X, player_O, player_X]
    grid = createNewGrid()
    while isgameOver == False:
        for player in playerTurns:
            print(grid)
            #print(type(playerTurns[player]))

            playerMove(playerTurns[player])

            rowWinCon()
            colWinCon()
            diagWinCon()
            
            if whoWon == player_X:
                isgameOver = True
            elif whoWon == player_O:
                isgameOver = True
            else:
                drawCon()

print("test")            
playTicTacToe()


# In[ ]:


print("test") 


# In[ ]:





# In[ ]:





# In[ ]:




