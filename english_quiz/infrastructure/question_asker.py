class QuestionAsker:
    def __init__(self, question, exact_answer, score_handler):
        self.question = question
        self.exact_answer = exact_answer
        self.score_handler = score_handler

    def ask_question(self):
        print(self.question)
        answer = self._get_user_answer()
        if self.is_answer_correct(answer=answer):
            print("Correct")
            self.score_handler.increment_score()
        else:
            print("Wrong")

    @staticmethod
    def _get_user_answer():
        answer = input('> ')
        return answer

    def is_answer_correct(self, answer):
        return self.exact_answer.lower() == answer.lower()
