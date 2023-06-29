from tkinter import *
from tkinter import Tk

from list_question import *


class QuizeUI:
    window: Tk = None
    qlabel = None
    ilabel = None
    rlabel = None
    questionBanks = None
    currentPosition = -1
    currentQuestion = None

    rad1 = None
    rad2 = None
    rad3 = None
    rad4 = None

    def __init__(self):
        self.window = Tk()

        # question label
        self.qlabel = Label(self.window, width=100, text="", fg="blue")
        self.qlabel.pack()

        # image label
        self.ilabel = Label(self.window)
        self.ilabel.pack()
        Label(self.window, text="Choose the correct answer and click [Next Question]").pack()

        # Correct/Incorrect result label
        self.rlabel = Label(self.window, text='')
        self.rlabel.pack()
        frame = Frame(self.window)
        self.radVars = StringVar(frame, "<none>")
        # rad 1
        self.rad1 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad1.grid(row=0, column=0)
        # rad 2
        self.rad2 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad2.grid(row=0, column=1)
        # rad 3
        self.rad3 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad3.grid(row=0, column=2)
        # rad 4
        self.rad4 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad4.grid(row=0, column=3)
        frame.pack()

        # Next Problem
        Button(self.window, text="New Question", command=self.checkAnswerAndMoveNextQuestion).pack()

        self.questionBanks = ListQuestion()
        if not self.questionBanks.isEmpty():
            self.currentPosition = 0
            self.showQuestion()

    # this function use to show the value of radiobutton when user selection
    def selection(self):
        s = "You selected the option [" + str(self.radVars.get()) + "]"
        self.rlabel.config(text=s, fg='blue')

    # This function use to show the next question and
    def showQuestion(self):
        self.currentQuestion = self.questionBanks.getQuestion(self.currentPosition)
        self.qlabel.config(text=self.currentQuestion.problemContent)
        img = PhotoImage(file=self.currentQuestion.image).subsample(2, 2)
        self.ilabel.config(image=img)
        self.ilabel.image = img
        ramdomAnswers = self.questionBanks.sample(self.currentPosition)
        self.rad1.config(text=ramdomAnswers[0].problemAnser, value=ramdomAnswers[0].problemAnser)
        self.rad2.config(text=ramdomAnswers[1].problemAnser, value=ramdomAnswers[1].problemAnser)
        self.rad3.config(text=ramdomAnswers[2].problemAnser, value=ramdomAnswers[2].problemAnser)
        self.rad4.config(text=ramdomAnswers[3].problemAnser, value=ramdomAnswers[3].problemAnser)
        self.currentPosition += 1

    # this function use to the  result of the current question
    def checkAnswerAndMoveNextQuestion(self):
        if self.currentQuestion is None:
            return
        if self.currentQuestion.isCorrect(str(self.radVars.get())) is True:
            self.rlabel.config(text="You are right", fg='blue')
        else:
            self.rlabel.config(text="You are wrong!", fg='red')
        if self.currentPosition >= self.questionBanks.sizeOfList():
            self.currentPosition = 0
        self.radVars.set("<none>")
        self.showQuestion()

    # this function use to set the screen is center of the desktop
    @staticmethod
    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    # this function use to show the GUI of the Quiz
    def showUI(self):
        # Take the quiz
        self.window.title("Take the quiz- Improved")
        self.window.geometry("550x400")
        self.center(self.window)
        self.window.mainloop()


# call showUI() to start the program
QuizeUI().showUI()
