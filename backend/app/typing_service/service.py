class TypingService:

    def type_text(self, text):
        from pynput.keyboard import Controller

        keyboard = Controller()
        keyboard.type(text)
