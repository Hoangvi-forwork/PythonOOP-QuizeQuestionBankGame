import random
from file_factory import FileFactory
from questions import Question


class ListQuestion:
    questions = set()

    def __init__(self):
        datas = FileFactory().readData()
        for item in datas:
            arrDataOfItem = item.strip().split(":")
            if len(arrDataOfItem) == 3:
                question = Question(arrDataOfItem[0],
                                    arrDataOfItem[1],
                                    arrDataOfItem[2])
                self.questions.add(question)

    # this function check the listquestion is empty or not
    def isEmpty(self):
        return len(self.questions) <= 0

    # this function return question at index position
    def getQuestion(self, index):
        if self.isEmpty():
            return None
        if index < 0 or len(self.questions) <= index:
            return None
        return list(self.questions)[index]

    def sample(self, index):
        currentQuestion = self.getQuestion(index)
        currentSet = set()
        currentSet.add(currentQuestion)
        remainList = list(self.questions - currentSet)

        samples = random.sample(remainList, 3)
        samples.append(currentQuestion)
        random.shuffle(samples)
        return samples

    def sizeOfList(self):
        return len(self.questions)
