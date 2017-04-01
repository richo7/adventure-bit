---
layout: default
---
# Microbattle

## Introduction

[Download](/games/microbattle/dist/microbattle.hex)

Microbattle is a game designed for use with the microbit.

The game requires 2 microbits, designed for use with 2 players

The overall idea of the game is to battle by entering the correct sequence before your opponent.

There are 2 ways to play your move, these are; attack and block. The options correspond to the respective buttons.

Then attack or block is selected, the player will be presented with a 5 or 4 letter series respectively which has to be correctly entered in time in order for it to effect their opponent.

In order of the move to be successful the sequence must be completed before the opponent.

Each player has a total of 5 lives for the duration of the game.

A successful attack will deduct a life from the opponent, a successful block will mean the attack makes no difference to the number of lives.

If both players were to perform their move successfully and at the same time, neither will receive any damage.

The goal of the game is to rid the opponent of their lives.

The game is over once a player loses all of their lives.</p>

## Explanation of method

After showing a brief animation which shows A/B scrolling past, a main menu is displayed

The menu shows the letter "L" in order to indicate that it is displaying lives and below that the bottom row of LED's light up in accordance to the number of lives the player has remaining

The game uses a base 'while' loop to poll each microbit for user input

Depending on which button has been pressed, different parameters are passed to the function responsible for sequence handling - the parameter numberOfMoves is passed in as 5 if the player attacks, and is passed in as 4 if the player blocks.

The function responsible for generating random sequences of length equal to numberOfMoves is called, to generate the sequence for each player.

This sequence is displayed and the program waits for user input from one of the two buttons and checks whether the user input is correct, given the sequence generated.

At the same time, the program checks to see whether a signal has been received from the opponent's microbit, which would indicate that they have successfully completed a move

In this case, the sequence will be cancelled and damage calculation will be entered.

If a signal is not received during this time, the program transmits a signal to the opponent's microbit to indicate that they have finished their move.

This cancels the opponent's move and goes directly to damage calculation.

Lives are deducted as described above and the main menu is displayed again.

If either player's lives reach 0, a message indicating winning/losing is displayed on the appropriate player's screen and the game exits.
