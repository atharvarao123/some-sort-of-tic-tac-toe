#Tic - Tac Toe Game
#3 by 3
# X , O
#if you want to play the Game
#After one choice the next choice should come
#Actually validating if it is a win
#Some sort of list for the board
import os
row1 = ["-","-","-"]
row2 = ["-","-","-"]
row3 = ["-","-","-"]
def print_board(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    print("This is the Initial board")


def game(row1,row2,row3):
    print("Starting Game")
    print("The two options are X and O")
    winstatus = False
    while winstatus == False:
        print(" Enter x or o")
        player1inp = input()
        print(player1inp)
        
        print(" enter your square")
        player1square= input()
        player1squareint = int(player1square)

        print("enter row ")
        player1row = input()
        player1rowint = int(player1row)
        
        if(player1row == "1"):
            if(row1[player1squareint] != "-"):
                print("Square is occupied")
            else:    
                row1[player1squareint] = player1inp
                print(row1)
                print(row2)
                print(row3)
        if(player1row == "2"):
            if(row2[player1squareint] != "-"):
                print("Square is occupied")
            else:
                row2[player1squareint] = player1inp
                print(row1)
                print(row2)
                print(row3)
        if(player1row == "3"):
            if(row3[player1squareint] != "-"):
                print("Square is occupied")
            else:
                row3[player1squareint] = player1inp
                print(row1)
                print(row2)
                print(row3)

        if(row1[0] and row2[1] and row3[2] == "x"):
            print("X wins the game")
            winstatus = True
            print(row1,row2,row3)    
        if(row1[0] and row1[1] and row1[2] == "x"):
            print("X wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row2[0] and row2[1] and row2[2] == "x"):
            print("X wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row3[0] and row3[1] and row3[2] == "x"):
            print("X wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row1[0] and row2[0] and row3[0] == "x"):
            print("X wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row1[1] and row2[1] and row3[1] == "x"):
            print("X wins the game")
            winstatus = False
            print(row1,row2,row3)
        if(row1[2] and row2[2] and row3[2] == "x"):
            print("X wins the game")
            winstatus = False
            print(row1,row2,row3)
        if(row1[2] and row2[1] and row3[0] == "x"):
            print("X wins the gmae")
            winstatus = False
            print(row1,row2,row3)
        


        if(row1[0] and row2[1] and row3[2] == "o"):
            print("o wins the game")
            winstatus = True
            print(row1,row2,row3)    
        if(row1[0] and row1[1] and row1[2] == "o"):
            print("o wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row2[0] and row2[1] and row2[2] == "o"):
            print("o wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row3[0] and row3[1] and row3[2] == "o"):
            print("o wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row1[0] and row2[0] and row3[0] == "o"):
            print("o wins the game")
            winstatus = True
            print(row1,row2,row3)
        if(row1[1] and row2[1] and row3[1] == "o"):
            print("o wins the game")
            winstatus = False
            print(row1,row2,row3)
        if(row1[2] and row2[2] and row3[2] == "o"):
            print("o wins the game")
            winstatus = False
            print(row1,row2,row3)
        if(row1[2] and row2[1] and row3[0] == "o"):
            print("o wins the gmae")
            winstatus = False
            print(row1,row2,row3)








print("Welcome To Tic Tac Toe - by atharva rao")
choice = True
while choice == True:
    def gameonoroff(choice,row1,row2,row3):
        print("Do you want to play Tic Tac Toe?")
        answer = input()
        if answer == "YES":
            game(row1,row2,row3)
        if answer == "No":
            exit()
        #else:
            #print("Invalid Input")

    gameonoroff(choice,row1,row2,row3)
