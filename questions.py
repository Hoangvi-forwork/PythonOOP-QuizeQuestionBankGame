class Question:
    problemContent = None
    problemAnser = None
    image = None

    def __init__(self, problemContent, problemAnser, image):
        self.problemContent = problemContent
        self.problemAnser = problemAnser
        self.image = image

    def isCorrect(self, answer):
        return self.problemAnser == answer

