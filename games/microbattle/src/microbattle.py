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
