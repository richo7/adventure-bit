from microbit import Image, display, sleep, button_a, button_b


class Boss:

    def __init__(self, comm):
        self.comm = comm
        self.max_health = 9
        self.health = self.max_health
        self.attack = 10
        self.level = 2
        self.defence = 2
        self.sp_defence = 2

    def take_damage(self, response):
        if response["command"] == "phys_attack":
            damage = int(response["value"]) // self.defence
        elif response["command"] == "magic_attack":
            damage = int(response["value"]) // self.sp_defence
        else:
            return
        self.health -= int(damage)
        if self.health <= 0:
            self.comm.send_command("end_fight", 1)

    def display_health(self):
        lights = self.health*10
        board = [["0" for x in range(5)] for y in range(5)]
        for i in range(5):
            if lights >= i * 20 + 20:
                board[0][i] = "9"
        return Image(':'.join([''.join(vals) for vals in board]))

    def aoe_attack(self):
        self.comm.send_command("enemy_attack", self.level)

    def attack(self):
        self.aoe_attack()

    def wake(self):
        self.comm.send_command("start_fight", 1)
        display.show(Image("00900:00900:00900:00000:00900"))
        sleep(500)
        for x in range(11):
            display.show(Image.ANGRY.shift_right(x - 5))
            sleep(200)

    def start(self):
        while True:
            resp = self.comm.wait_for_command(0)
            if resp["command"] == "start_fight":
                while not resp["command"] == "end_fight":
                    resp = self.comm.wait_for_command(0)
                    if button_a.is_pressed() or button_b.is_pressed():
                        display.scroll("Finish fight...")
            if button_a.is_pressed() or button_b.is_pressed():
                self.wake()
                break
        while self.health > 0:
            display.show(self.display_health())


if __name__ == '__main__':
    comm = Comm(42, group=1)
    boss = Boss(comm)
    boss.start()
