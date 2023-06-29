# class FileFactory:
#     questionBank = r'.\data_exercise30\problem.txt'
#     encoding = 'utf8'
#     mode = 'r'
#
#     # read the content of file
#     def readData(self):
#         file = open(self.questionBank, self.mode, encoding=self.encoding)
#         datas = file.readlines()
#         file.close()
#         return datas

class FileFactory:
    questionBank = r'.\data_exercise30\problem.txt'
    encoding = 'utf8'
    mode = 'r'

    # read the content of file
    def readData(self):
        file = open(self.questionBank, self.mode, encoding=self.encoding)
        datas = file.readlines()
        file.close()
        return datas
