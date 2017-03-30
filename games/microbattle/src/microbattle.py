from microbit import *
#Adds commands to control microbit LEDs and display
import random.randint
#Import random to be able to create randomised sequences
import radio
#Import radio to allow bluetooth communication between microbits
seq1 = Image("00000:00000:90000:00000:00000")
seq2 = Image("00000:00000:99000:00000:00000")
seq3 = Image("00000:00000:99900:00000:00000")#Creates a sequence of images to display the current input the player is on
seq4 = Image("00000:00000:99990:00000:00000")
seq5 = Image("00000:00000:99999:00000:00000")
seqlist = [seq1, seq2, seq3, seq4, seq5]
#Groups the different images into a list
l1 = Image("09000:09000:09990:00000:00009")
l2 = Image("09000:09000:09990:00000:00099")
l3 = Image("09000:09000:09990:00000:00999")#Creates a sequence of images to represent the player health
l4 = Image("09000:09000:09990:00000:09999")
l5 = Image("09000:09000:09990:00000:99999")
liveslist = [l1, l2, l3, l4, l5]
#Groups the different images into a list
lives = 5
#Defauts the number of lives to 5
radio.on()
#Turns the radio on
radio.config(channel=72)
#Configures the radio to broadcast and recieve using channel 72 to not interfere with other Microbits


def sequence(numberOfMoves, word):
#Creates a function that creats a random sequence of A's and B's
    for i in range(0, numberOfMoves):
    #This will create a number of random letters depending on the move type chosen
        randnum = random.randint(0, 1)
        #This will choose a random binary number to represent A and B
        if randnum == 0:
            word += "A"
        #If the randomly chosen number is 0, it sets the next letter in the sequence to A
        else:
            word += "B"
        #If the randomly chosen number is 1, it sets the next letter in the sequence to B
    display.scroll(word)
    #Displays the full sequence after it has been written
    return word
    #This will returjn the word variable


def move(typeOfMove, numberOfMoves, lives):
#Creates the function in charge of running the main sequence process
    radio.on()
    #Turns the radio on
    roundSuccess = True
    #It sets whether or not a person has completed the sequence before their opponent to True
    display.clear()
    #This will clear anything already on the display
    sleep(250)
    #This will add a delay so that the clear screen is shown for a visible time
    correct = True
    #This defaults the correct variable to True
    incoming = ""
    #This resets the variable each time the function is called
    if numberOfMoves != -1:
    #This is to test whether or not an exception is called to skip the sequence that comes after
        word = sequence(numberOfMoves, "")
        #Generates a word using the sequence function above
        for i in range(0, numberOfMoves):
        #Asks for button presses equal to the length of the sequence
            cond = False
            #Initialises the variable to run the while loop below
            while (cond is False):
            #While loop to wait for the user to press a button
                incoming = radio.receive()
                #Check if the other user has already completed their sequence
                if incoming is not None and incoming != "Fail":
                #If the sequence is already completed
                    cond = True
                    correct = False
                    roundSuccess = False
                    typeOfMove = "Fail"
                    i=numberOfMoves
                    break
                    #Set the variables to not re-enter the loop then break out of the loop
                elif button_a.is_pressed():
                #If the button a was pressed
                    cond = True
                    #Stop looping the wait for the button press
                    if word[i] == "B":
                    #If the user pressed the wrong button
                        display.show(Image.NO)
                        #Show a cross to the user to show they've gotten it wrong
                        correct = False
                        typeOfMove = "Fail"
                        break
                        #Set variables to not re-enter the loops and then break out of them
                    else:
                        display.show(seqlist[i])
                        #Otherwise the user got it right therefore the next light on the sequence, lights up
                elif button_b.is_pressed():
                #If the button b was pressed
                    cond = True
                    #Stop looping the wait for the button press
                    if word[i] == "A":
                    #If the user pressed the wrong button
                        display.show(Image.NO)
                        #Show a cross to the user to show they've gotten it wrong
                        correct = False
                        typeOfMove = "Fail"
                        break
                        #Set variables to not re-enter the loops and then break out of them
                    else:
                        display.show(seqlist[i])
                        #Otherwise the user got it right therefore the next light on the sequence, lights up
                sleep(200)
                #Wait 0.2 seconds between checking between button presses to differentiate the user holding down the button for a time and pressing the button
            if correct is False:
                break
            #If the variable is false, leave the loop
    else:
        roundSuccess = False
        correct = False
        typeOfMove = "Fail"
    #If the person did not complete their task then set the variables to show they've failed
    incoming = radio.receive()
    #Look for incoming Bluetooth signals to see if the other user has finished
    sleep(50)
    #Wait a time for Bluetooth transfer delay
    radio.send(typeOfMove)
    #Send the other user what type of move was preformed, Attack, Block or Failed Move
    while incoming is None:
        sleep(10)
        radio.send(typeOfMove)
        incoming = radio.receive()
    #If the other user has not sent their signal yet, then wait for their signal and send your signal repetitively until they send their data.
    display.scroll(typeOfMove[0] + " v " + incoming[0])
    #Display to the user that move they performed and the move the enemy user performed eg AvB (Attack vs Block)
    if correct is True:
    #If you haven't failed
        if incoming == "Attack" and typeOfMove == "Block":
        #And they attacked and you blocked
            if roundSuccess is False:
            #And they performed their attack first
                lives -= 1
                #Lose a life
        elif incoming == "Attack" and typeOfMove == "Attack":
        #If you attack and they attacked
            if roundSuccess is False:
            #And they performed their attack first
                lives -= 1
                #Lose a life
    else:
    #If you did fail
        if incoming == "Attack":
        #And they attacked
            lives -= 1
            #Lose a life
    display.show(str(lives))
    #Show to the user their lives on the microbit screen
    sleep(3000)
    #For 3 seconds
    return lives
    #Update the lives to main


#Start of program
display.scroll("A/B")
#When the program starts, show the user to press either A or B
while lives > 0:
#While you still have lives
    radio.on()
    #Turn the radio on and keep it on
    try:
        incoming = radio.receive()
    #Attempt to read bluetooth data
    except ValueError:
        incoming = None
    #If this is impossible, set the data to a Null type
    display.show(liveslist[lives-1])
    #Light up a number of LED's across the bottommost row equal to the number of lives you have
    if incoming is not None:
        if incoming != "Fail":
            if incoming == "0":
                display.show("WINNER ")
                break
            elif incoming == "Attack" or incoming == "Block":
                lives = move("Fail", -1, lives)
            else:
                pass
                #  Something went wrong :(
    elif button_a.is_pressed():
        lives = move("Attack", 5, lives)
    elif button_b.is_pressed():
        lives = move("Block", 4, lives)

if lives == 0:
    radio.on()
    display.show("LOSER ")
    while True:
        radio.send("0")
    
