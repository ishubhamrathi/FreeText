class HotkeyContext:

    def __init__(self):

        self.pressed = set()

    def press(self, key):

        self.pressed.add(key)

    def release(self, key):

        self.pressed.discard(key)

    def is_active(
        self,
        required
    ):

        return required.issubset(
            self.pressed
        )