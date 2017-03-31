from microbit import *
import random
import radio
points = 0
for i in range(0, 5):
    letter = random.randint(0, 1)
    if letter == 0:
        letter = "A"
    else:
        letter = "B"
    display.show(letter)
    cond = False
    while (cond is False):
        if button_a.is_pressed():
            cond = True
            display.clear()
            sleep(300)
            if letter == "A":
                points = points + 1
            else:
                display.show(Image.NO)
                sleep(300)
        elif button_b.is_pressed():
            cond = True
            display.clear()
            sleep(300)
            if letter == "B":
                points = points + 1
            else:
                display.show(Image.NO)
                sleep(300)
display.scroll(str(points))
radio.on()
radio.send(str(points))
while True:
    incoming = radio.receive()
    if incoming is not None:
        break
radio.send(str(points))
incoming = int(incoming)
if incoming < points:
    display.scroll("You win!")
elif incoming > points:
    display.scroll("You lose!")
else:
    display.scroll("Draw")
radio.off()
