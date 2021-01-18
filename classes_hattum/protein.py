class Protein:
    def __init__(self, code):
        self.code = code
        self.length = len(code)

    def pop_first_char(self):
        letter = self.code[0]
        self.code = self.code[1:]
        self.length = len(self.code)
        return letter