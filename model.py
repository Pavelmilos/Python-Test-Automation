class Question():

    def __init__(self, text="", code="", answer=None):
        self.text = text
        self.code = code
        self.answer = answer if answer else []

    def __str__(self):
        return f"{self.text} {self.code} {self.answer}"
