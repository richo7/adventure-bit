from microbit import display, sleep, button_a, button_b
import random


class Mage(Player):
    def __init__(self):
        super().__init__()
        self.maxHealth = 10
        self.health = self.maxHealth
        self.hitProb = 0.4
        self.classDamage = 4

    def generate_spell_chain(self):
        return [random.choice(("A", "B")) for _ in range(self.level)]

    def show_spell_chain(self, chain):
        display.clear()
        display.scroll("".join(chain))
        display.clear()

    def attack(self):
        actual_chain = self.generate_spell_chain()
        self.show_spell_chain(actual_chain)
        cast_chain = self.get_cast_spell()

        correct = 0
        for actual, cast in zip(actual_chain, cast_chain):
            if actual == cast:
                correct += 1

        if correct > self.level / 2:
            self.comm.send_command("magic_attack", self.level * self.classDamage)

    def get_cast_spell(self):
        chain = []
        for _ in range(self.level):
            if (button_a.get_presses() > 0):
                chain.append("A")
                display.show("A")
            elif (button_b.get_presses() > 0):
                chain.append("B")
                display.show("B")
        return chain

    def start(self):
        while self.health > 0:
            display.show(self.display_health())
            if button_a.is_pressed():
                self.attack()
            sleep(200)
        display.show(Player.DEAD)


if __name__ == '__main__':
    comm = Comm(42, group=1)
    warrior = Mage(comm)
    warrior.start()
