from english_quiz.infrastructure.question_asker import QuestionAsker
from english_quiz.infrastructure.score_handler import ScoreHandler
from english_quiz.infrastructure.table_retriever import TableRetriever


def main():
    score_handler = ScoreHandler()
    table = TableRetriever.get_table()

    while not table.is_empty():
        question, exact_answer = table.get_question_and_answer()
        question_asker = QuestionAsker(question=question, exact_answer=exact_answer, score_handler=score_handler)
        question_asker.ask_question()

    print(f'You got {score_handler.get_score()} points.')


if __name__ == '__main__':
    main()
