from microbit import *
#Get microbit commands to run and display
import random.randint
#Random Integer for creating randomised sequence
import radio
#Importing bluetooth support

points = 0
#Initialise the point so it can be incremented / decremented
for i in range(0, 5):
#Sequence of 5 presses so the code is run 5 times
    letter = random.randint(0, 1)
    #Assign a random number to a variable that will be converted to a letter
    if letter == 0:
        letter = "A"
        #Convert the letter to A if the random number was 0
    else:
        letter = "B"
        #Convert the letter to B otherwise as the only other value possible is 1
        #An error catch else was removed in order to save memory space for the microbit
    display.show(letter)
    #Display the letter to the user so they can copy it
    cond = False
    #Initilise variable to create a Do While loop
    while (cond is False):
    #Wait for any button to be pressed
        if button_a.is_pressed():
        #If the Left button (A) was pressed
            cond = True
            #End the while loop
            display.clear()
            #Clear the display of the letter displayed
            sleep(300)
            #Wait 0.3 seconds to continue so the same button press doesn't carry over
            if letter == "A":
            #If the correct button was pressed
                points += 1
                #Increase your points by 1 for getting it right
            else:
            #Otherwise
                display.show(Image.NO)
                sleep(300)
                #Display an X on the LEDs for 0.3 seconds and don't change points
        elif button_b.is_pressed():
        #If the Right button (B) was pressed, as above
            cond = True
            display.clear()
            sleep(300)
            if letter == "B":
                points = points + 1
            else:
                display.show(Image.NO)
                sleep(300)

display.scroll(str(points))
#Display to the user their points by making it go right to left across the LEDS
radio.on()
#Turn on bluetooth to communicate with other Microbit
radio.send(str(points))
#Send the other microbit your points to see who won or lost
incoming = None
while incoming is None:
    incoming = radio.receive()
#Create a do while loop that waits until the other Microbit sends their points back over bluetooth
radio.send(str(points))
#Send your points again so it does not matter which Microbit sends their points first
incoming = int(incoming)
#Convert the string value of the points to an integer; It was converted to string to transfer over Bluetooth
if incoming < points:
    display.scroll("You win!")
    #If you have more points than other Microbit, display win message
elif incoming > points:
    display.scroll("You lose!")
    #If you have less points than other Microbit, display lose message
else:
    display.scroll("Draw")
    #Otherwise the only other possibility is they have the same points, then display draw message
radio.off()
#Turn the bluetooth off as it is uneeded after information had been transfered
