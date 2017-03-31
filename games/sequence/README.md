---
laout: standard
---
# How the Game Works
The program imports the modules of random and radio (Bluetooth in micro:bit). 
The program picks a random letter from 0-1 which selects whether it is selected as A or B. 
The program demands that the micro:bit displays the letter. 
The program then waits for user input from one of the two buttons using while loop. 
If the button press matches the button displayed, then the user gains a score. 
Otherwise an X is displayed. 
This repeats 5 times using a for loop.
The bluetooth then signals to the other user their score.
If your score is above than theirs then You Win
If your score is lower than theirs then You Lose
If your scores are the same then you both Draw

# Problems 
Originally we were attempting to program the game in JavaScript/TypeScript using the online MicroBit editor, after attempting to create a while loop; we realised it did not work as intended so we attempted to use the block MicroBit program editor. This section did not have the functionality to run the game as we intended so we decided to swap to Python and upload that to the MicroBits instead. 

Another problem was having the Microbits send the their scores across bluetooth to eachother and having them both receive. We solved this problem by creating a while loop that sends and waits to recieve the bluetooth signal until they both have received the necessary data as well as signalling before and after the while loop incase.
