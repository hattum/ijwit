class Protein:
    """
    Protein returns the subsequent letters
    of the amino acid sequence one by one(queue).
    """
    def __init__(self, code):
        self.code = code
        self.length = len(code)

    def pop_first_char(self):
        """
        Returns the first amino acid in the list.
        """
        letter = self.code[0]
        self.code = self.code[1:]
        self.length = len(self.code)
        return letter
