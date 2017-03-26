from microbit import display, sleep, button_a


class Warrior(Player):

    def __init__(self, comm):
        super().__init__(comm)
        self.maxHealth = 20
        self.health = self.maxHealth
        self.hitProb = 1
        self.classDamage = 2

    def start(self):
        while self.health > 0:
            display.show(self.display_health())
            if button_a.is_pressed():
                self.attack()
            sleep(500)
        display.show(Player.DEAD)


if __name__ == '__main__':
    comm = Comm(42, group=1)
    warrior = Warrior(comm)
    warrior.start()
