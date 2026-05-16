from pynput.keyboard import Controller


keyboard = Controller()


class TypingService:

    def type_text(self, text):
        keyboard.type(text)
