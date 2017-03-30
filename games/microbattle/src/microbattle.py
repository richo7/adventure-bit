from microbit import *
import random
import radio
word = ""
seq1 = Image("00000:00000:90000:00000:00000")
seq2 = Image("00000:00000:99000:00000:00000")
seq3 = Image("00000:00000:99900:00000:00000")
seq4 = Image("00000:00000:99990:00000:00000")
seq5 = Image("00000:00000:99999:00000:00000")
seqlist = [seq1, seq2, seq3, seq4, seq5]
l1 = Image("09000:09000:09990:00000:00009")
l2 = Image("09000:09000:09990:00000:00099")
l3 = Image("09000:09000:09990:00000:00999")
l4 = Image("09000:09000:09990:00000:09999")
l5 = Image("09000:09000:09990:00000:99999")
liveslist = [l1, l2, l3, l4, l5]
lives = 5
radio.on()
radio.config(channel=72)


def sequence(numberOfMoves, word):
    for i in range(0, numberOfMoves):
        randnum = random.randint(0, 1)
        if randnum == 0:
            word += "A"
        else:
            word += "B"
    display.scroll(word)
    return word


def move(typeOfMove, numberOfMoves, lives):
    radio.on()
    roundSuccess = True
    display.clear()
    sleep(250)
    correct = True
    incoming = ""
    if numberOfMoves != -1:
        word = sequence(numberOfMoves, "")
        for i in range(0, numberOfMoves):
            cond = False
            while (cond is False):
                incoming = radio.receive()
                if incoming is not None and incoming != "Fail":
                    cond = True
                    correct = False
                    roundSuccess = False
                    typeOfMove = "Fail"
                    i=numberOfMoves
                    break
                elif button_a.is_pressed():
                    cond = True
                    if word[i] == "B":  # User got wrong
                        display.show(Image.NO)
                        correct = False
                        typeOfMove = "Fail"
                        break
                    else:
                        display.show(seqlist[i])
                elif button_b.is_pressed():  # User got wrong
                    cond = True
                    if word[i] == "A":
                        display.show(Image.NO)
                        correct = False
                        typeOfMove = "Fail"
                        break
                    else:
                        display.show(seqlist[i])
                sleep(200)
            if correct is False:
                break
    else:
        roundSuccess = False
        correct = False
        typeOfMove = "Fail"
    incoming = radio.receive()
    sleep(50)
    radio.send(typeOfMove)
    while incoming is None:
        sleep(10)
        radio.send(typeOfMove)
        incoming = radio.receive()
    display.scroll(typeOfMove[0] + " v " + incoming[0])
    if correct is True:
        if incoming == "Attack" and typeOfMove == "Block":
            if roundSuccess is False:
                lives -= 1
        elif incoming == "Attack" and typeOfMove == "Attack":
            if roundSuccess is False:
                lives -= 1
    else:
        if incoming == "Attack":
            lives -= 1
    display.show(str(lives))
    sleep(3000)
    return lives


display.scroll("A/B")
while lives > 0:
    radio.on()
    try:
        incoming = radio.receive()
    except ValueError:
        incoming = None
    display.show(liveslist[lives-1])
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
    
