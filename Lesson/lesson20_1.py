import string


class Alphabet:
    def __init__(self, language, letters):
        self.lang = language
        self.letters = letters

    def print(self):
        print(self.letters)

    def letterns_num(self):
        print(len(self.letters))

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('en', string.ascii_uppercase)

    def is_in_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letterns_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("English example:\nI writing this text using eng alphabet")


a = Alphabet('rus', 'ага')
a.letterns_num()
eng = EngAlphabet()
print(eng.is_in_letter('s'))
eng.example()
