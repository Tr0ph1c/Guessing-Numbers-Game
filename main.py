from random import randint
num = 0
pts = 0
tries = 0

def entry():
    print("Welcome to this retarded game where you have to guess a number between 2-30 (both inclusive)\n\n")
    input("PRESS ANY KEY TO CONTINUE")
    main()

def main():
    global num
    global tries
    tries = 0
    num = randint(2, 30)
    print("Guess the number!")
    guess()

def guess():
    global num
    ans = input()
    if (ans == str(num)):
        win()
    elif (ans == "give"):
        print(num)
        print("GAME RESTARTED....")
        main()
    else:
        lose()

def win():
    global pts
    global tries
    print("You got it right!")
    pts += 1
    print("YOUR POINTS: ", str(pts))
    print("YOU GUEESSED IN: ", tries+1, "tries.")
    input("PRESS ANY KEY TO CONTINUE")
    main()
    
def lose():
    global pts
    global num
    global tries
    tries += 1
    if (tries==6):
        finguesses()
    if (tries==7):
        die()
    print("Not the right number")
    if (tries==3):
        hint = gethint(num)
        print("HINT:", hint)
    guess()

def finguesses():
    global pts
    print("You guessed 6 times incorrectly, 1 try remaining.")
    input("PRESS ANY KEY TO CONTINUE WITH YOUR LAST GUESS")
    print("LAST GUESS: ")
    guess()

def die():
    global pts
    global tries
    HSFile = open("highscore.txt", "r")
    oldHS = int(HSFile.read())
    HSFile.close()
    if (pts>oldHS):
        HSFileW = open("highscore.txt", "w")
        HSFileW.write(str(pts))
        HSFileW.close()
        HS=pts
        print("\n\nNEW HIGHSCORE!\n")
    HS=oldHS
    print("\nGAME OVER\n\n")
    print("YOUR SCORE: ", pts)
    if (pts>oldHS):
        print("PREVIOUS HIGH SCORE: ", HS, "\n")
    else:
        print("HIGH SCORE: ", HS, "\n")
    input("PRESS ANY KEY TO RESTART")
    print("\n\n\n\n\n")
    pts = 0
    tries = 0
    main()

def gethint(n):
    text = "It is a number "
    if (n%10==0):
        text+="that has a zero at its end."

    elif (n%5==1):
        text+="when divided by 5, gives a remainder of 1."
        
    elif (n%2==0 and n!=0):
        text+="divisable by 2 and has no 0 or 6 in it."

    elif (str(n)[-1]=='3' or str(n)[-1]=='7'):
        text="It ends in either 3 or 7."

    elif (n%5==0):
        text="It is a multiple of 5."

    else:
        text+="with a nine in it."
    
    return text

entry()
