import random

from microbit import Image, display, sleep


class Player:
    SHIELD = Image("99999:99999:90909:09090:00900")
    DEAD = Image("90009:09090:00900:09090:90009")

    CRIT_ANIMATION = [
        Image("00900:00900:00900:09990:00900"),
        Image("90909:00900:00900:09990:90909"),
        Image("00900:00900:00900:09990:00900"),
        Image("90909:00900:00900:09990:90909")]

    def __init__(self, comm):
        self.comm = comm
        self.level = 3
        self.maxHealth = 20
        self.health = self.maxHealth
        self.hitProb = 0.6
        self.damageReduction = 1
        self.classDamage = 1

    def start(self):
        while self.health > 0:
            display.show(self.display_health())
            sleep(100)
        display.show(Player.DEAD)

    def attack(self):
        self.comm.send_command("phys_attack", self.level * self.classDamage)

    def take_damage(self, damage):
        if (random.randint(0, 10) / 10.0) <= self.hitProb:
            self.health -= (int(damage))
        else:
            pass
            display.show(Player.SHIELD)
            sleep(500)

    def display_health(self):
        lights = int((self.health/float(self.maxHealth))*100)
        board = [["0" for x in range(5)] for y in range(5)]
        for i in range(5):
            if lights >= i * 20:
                board[0][i] = "9"
        return Image(':'.join([''.join(vals) for vals in board]))
