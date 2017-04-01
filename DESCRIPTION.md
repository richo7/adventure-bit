PRISONERS DILEMMA:

How to access:

1. Download the 'microbit-finishedMain.hex' file in ;
2. Copy the .hex file onto your microbit;
3. You're done!


How to play:

You will be presented with a 'V' on start up, which stands for 'Verification'.
1. Press 'A' button to turn that micro-bit into a player, or the 'B' button to
   turn that micro-bit into a computer.
2. Once two micro-bit's have been verified, the turn number (which will be one)
   will be displayed on the micro-bit awaiting for your decision. Press either
   'A' at this point to be 'SILENT' or 'B' to 'BETRAY'. 
3. If playing an AI, choosing your choice will immediately show the scores in a
   'x : y' format, where 'x' is your score and 'y' is your opponents. If playing
   another player, this won't happen until both players have pressed a button.
4. After the alotted amount of rounds, you will either be presented with a
   scrolling 'WIN', 'LOSE' or 'DRAW' depending on whether you won, lost or drew.
   This will then be followed by the final score.
5. Once you have finished a game, your must pressed the 'RESET' button on the back
   of the micro-bit to return to the verification stage.
   

How to make changes:

While the code is heavily commented, the following will outline some of the main
changes you may want to make to the game.

Adding Strategies:
Each strategy begins with the same code each time to initiate the strategy. For this
you want to add the following code to begin coding the strategy:

class StrategyN extends Strategy {

    constructor(ai: Ai) {
        super(ai)
    }

    getNextMove(): boolean {

(where N in 'StrategyN' is 1 above the previous Strategy)
	
Once you have this, you want to code your strategy into the getNextMove() function. 
In this function:

- You'll want to use the line of code:

let enemyMoves = this.parentAi.getEnemyMoves()

  in order for the AI to know what the player chose to do last turn.
  
- If you need to know the current round, use the line of code:

let currentRound = enemyMoves.length + 1;

  to get it. This essentially checks the length of the array that stores the players
  choices; this value + 1 will be give the current turn you are on, as the player has
  a choice each turn and is indexed, so adding will will unindex it.
  
- Add any further code you need to write in order to complete the strategy.

Finally, once you have finished the strategy code, you want to go up to 'Class Ai' and
look for the lines with code that looks like:

this.strategies.push(new Strategy1(this)).

Once you have found this part in the file, you want to add a new line under the last line
that looks like the one above and re-write it, with the 'Strategy1' being replaced for the
name of the 'Strategy' function you have just written. For example, if I was to add
'Strategy7', I will add:

this.strategies.push(new Strategy7(this)).

Changing the number of rounds:
At the top of the code, there will be a line of code that says:

const MAX_ROUNDS = 5 (set to 5 by default).

To change the amount of rounds there are, change the number 5 to the number of rounds you
wish to play a save it.

Once you have made changes:
Once you have made any changes, save the file and recompile it into a .hex file using the
microbit.com website. This file is then the file you need to drag onto your micro-bit in
order to play it.


Improvements:

The current version of the game does need further improvements. These improvments include:

1. Further strategies are need to give the game more variety. There are currently 6 strategies
   that have been implemented, most of which are relativley simple or similar to another strategy
   that is implemented. 
   
   Feel free to add further strategies using the guide above.