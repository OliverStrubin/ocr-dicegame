#Imports needed
import random
import time

global player1
global player2
P1Score = 0
P2Score = 0

#File Login System 
def loginPlayerOne():
    global player1
    print("P1 please enter your account information.")
    time.sleep(1)
    UserName = str(input("Username: "))
    Password = str(input("Password: "))
    account = open("accounts.txt", "r")
    accounts  = account.readlines()
    for lines in accounts:
        acc_details = lines.split(",")
        acc_password = acc_details[1].split("\n")
        if acc_details[0] == UserName:
            if acc_password[0] == Password:
                print("Hello, ",UserName)
                player1 = UserName
                isLogin = True
    if isLogin == False:
        print ("Incorrect details! Try again.")

#File Login System 
def loginPlayerTwo():
    global player2
    print("P2 please enter your account information.")
    time.sleep(1)
    UserName = str(input("Username: "))
    Password = str(input("Password: "))
    account = open("accounts.txt", "r")
    accounts  = account.readlines()
    for lines in accounts:
        acc_details = lines.split(",")
        acc_password = acc_details[1].split("\n")
        if acc_details[0] == UserName:
            if acc_password[0] == Password:
                print("Hello, ",UserName)
                player2 = UserName
                isLogin = True
    if isLogin == False:
        print ("Incorrect details! Try again.")

#The game itself
def game():
    global P1Score
    global P2Score
    print(player1 + " Round: " + str(roundNumber))
    input("Press any key to roll the dice.")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    time.sleep(1)
    print("Rolling the dice...")
    time.sleep(1)
    print("You rolled: " + str(dice1)) #Dice 1
    time.sleep(1)
    print("You rolled: " + str(dice2)) #Dice 2
    dice_total = dice1 + dice2
    time.sleep(1)
    print("Your total: " + str(dice_total))
    if (dice_total % 2) == 0: #Checking if dice roll is even
        print("Your total is even. You've been awarded with 10 more points.")
        P1Score = dice_total + P1Score + 10
        print("Your total points: " + str(P1Score))
    else: #Dice roll is odd
        print("Uh oh your total is odd. 5 points have been removed from your score.")
        P1Score = P1Score - 5
        if P1Score < 0: #Checking if points are below 0 and if so setting them to 0
            P1Score = 0
        print(player1 + " your total points: " + str(P1Score))
    if dice1 == dice2: #Checking if the player rolled a double
        print("You rolled a double! You can now roll again.") 
        time.sleep(0.5)
        input("Press any key to roll again. ")
        dice3 = random.randint(1,6)
        time.sleep(1)
        print("Rolling...")
        time.sleep(1)
        print("You rolled: " + str(dice3))
        P1Score = P1Score + dice3 #Adding the other dice to the score
        if P1Score < 0:
            p1Score = 0
        print(player1 + " You are now on: " + str(P1Score))
        #======================================================== THE EXACT SAME BUT FOR PLAYER2
    print(player2 + " Round: " + str(roundNumber))
    input("Press any key to roll the dice.")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    time.sleep(1)
    print("Rolling the dice...")
    time.sleep(1)
    print("You rolled: " + str(dice1))
    time.sleep(1)
    print("You rolled: " + str(dice2))
    dice_total = dice1 + dice2
    time.sleep(1)
    print("Your total: " + str(dice_total))
    if (dice_total % 2) == 0:
        print("Your total is even. You've been awarded with 10 more points.")
        P2Score = dice_total + P2Score + 10
        print("Your total points: " + str(P2Score))
    else:
        print("Uh oh your total is odd. 5 points have been removed from your score.")
        P2Score = P2Score - 5
        if P2Score < 0:
            P2Score = 0
        print(player2 + " your total points: " + str(P2Score))
    if dice1 == dice2:
        print("You rolled a double! You can now roll again.")
        time.sleep(0.5)
        input("Press any key to roll again. ")
        dice3 = random.randint(1,6)
        time.sleep(1)
        print("Rolling...")
        time.sleep(1)
        print("You rolled: " + str(dice3))
        P2Score = P2Score + dice3
        if P2Score < 0:
            p2Score = 0
        print(player2 + " You are now on: " + str(P2Score))

loginPlayerOne() #When program starts user is prompoted to enter username & password
loginPlayerTwo() #When program starts user2 is promoted to enter username & password
for roundNumber in range(1,6): #Keeps track of which round they're on
    game()

if (P1Score == P2Score): #Checks if sudden death is needed. 
    print("SUDDEN DEATH!!!")
    time.sleep(1)
    print("Rules:")
    print("1) Both players will roll")
    print("2) Whoever has the highest roll wins")
    time.sleep(1)
    input(player1 + " Press any key to roll the dice. ")
    sudd_dice_one = random.randint(1,6)
    print(player1 + "You rolled: " + str((sudd_dice_one)))
    time.sleep(1)
    input(player2 + " Press any key to roll the dice. ")
    sudden_dice_two = random.ranint(1,6)
    print(player2 + "You rolled: " + str(sudden_dice_two))
    if(sudden_dice_one < sudden_dice_two): #Checks which player got the most points during sudden death
        print(player2 + " won!")
    else:
        print(player1 + " won!")
else:
    if(P1Score < P2Score): #Checks who wins the game and announces the winner.
        print(player2 + " wins the game.")
    else:
            print(player1 + " wins the game.")
