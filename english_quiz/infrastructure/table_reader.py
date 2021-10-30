class TableReader:
    def __init__(self, data):
        self.data = data

    def is_empty(self):
        return self.data.shape[0] == 0

    def get_question_and_answer(self):
        question_row = self.data.sample(n=1)
        self.data = self.data.drop(question_row.index)
        question, exact_answer = question_row['french'].iloc[0], question_row['english'].iloc[0]
        return question, exact_answer
