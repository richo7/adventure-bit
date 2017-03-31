## MicroBattle

# Installing the game
In order to install the game
1   Download the .hex file in the dist folder
2   Plug in your MicroBit to your computer via USB to MicroUSB
3   Wait for the computer to detect the external harddrive of the MicroBit
4   Transfer the file to the MicroBit where it will automatically write to its internal memory
5   Repeat the steps above for another MicroBit
6   Plug in the batteries and play

# Playing the game
When the game starts it will display the 5 lives you currently have at the bottom of the screen
You will have two options of either (A)ttack and (B)lock
To do any move, you must enter in a sequence of As and Bs displayed at the beginning
The attack move requires you to repeat 5 letters in the sequence
The block move requires you to repeat 4 letters in the sequence

Whoever finishes their move first (by a significant portion of time) causes the other to fail

If you successfully attack then the opponent will lose a life
If you successfully block then you cannot lose a life
If you both finish your attack within a close time period will cause a parry where no damage is done
If you attack and block within a close time period, the attack will be blocked
If you both finish your block within a close time period, both blocks go off and no damage is dealt

## How it works 

The code is split into two functions - one which generates random sequences of a length defined by the parameter numberOfMoves, and one which handles user input (checking this against the generated sequence). The function 'sequence()' is very similar to that used in the game 'sequence'; we have built on our Minimum Value Project to make Microbattle.
There is also a main loop which polls the microbit for user input, as well as checking whether the opponent's microbit is broadcasting a lose signal, in which case it displays the message 'WINNER' and halts.

If the button 'a' is pressed, the function 'move()' is called, and the values "attack", 5 and the variable lives are passed to it. This reduces the use of global variables, as well as allowing for reduction in code size. If the button 'b' is pressed, the function move() is also called, but this time it is passed a value of 4. This means that the sequence length for an attack is 5 letters long, but the sequence length for a block is only 4 letters long, to encourage the player to block. 
Inside the function 'move()', the microbit is also polled for input, after the randomly generated list is displayed. At the same time, it checks to see whether the opponent's microbit has broadcast a signal, which would indicate that it has finished its move, and, if so, breaks out of the sequence entering and goes directly to damage calculation, to reduce the length of the game.
If a player enters their sequence before the opponent, their microbit will broadcast a signal via bluetooth and wait to receive one, then enter damage calculation.
Lives are deducted as described above and, if a player reaches 0 lives, the game ends (with messages displayed as earlier).

## Improvements

Here's a list of things that could be done to make this repo/website better.

- Add further explaination to the readme.md and index.html
- If both A and B are both pressed at the same time, do a special move
    - Special move could require 7 letter sequence
    - Special move could require doing physical gestures like moving the Microbit up and down, or shaking it
    - Special move could deal 2 to 3 damage, may be unbalanced
    - How to balance the special move
- Add a feature that doesn't display the sequence till after the enemy has also chosen a move so both start at the same time
- Balancing
    - Balancing the parry feature by decreasing the timeframe 
    - Balancing the block button by lengthening the attack sequence or decreasing the length of the block sequence
