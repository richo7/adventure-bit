import radio


class Comm:
    def __init__(self, group):
        self.group = group
        radio.on()
        radio.config(group=group, queue=10)

    def send_command(self, command, value):
        vals = {}
        vals["command"] = command
        vals["value"] = value
        data = ":".join([str(x) + "," + str(vals[x]) for x in vals])
        radio.send(data)

    def wait_for_command(self, blocking=1):
        if blocking:
            while True:
                msg = radio.receive()
                if msg:
                    break
        else:
            msg = radio.receive()
        if not msg:
            return {"command": "", "value": ""}
        vals = msg.split(":")
        data = {}
        for x in vals:
            key, value = x.split(",")
            data[key] = value
        return data
