import pytest

from english_quiz.infrastructure.question_asker import QuestionAsker
from english_quiz.infrastructure.score_handler import ScoreHandler

DATA_TEST = [
    ('coarse', 'Coarse'),
    ('coarse', 'COARSE')
]


@pytest.mark.parametrize('exact_answer,given_answer', DATA_TEST)
def test_is_answer_correct(exact_answer, given_answer):
    # Given
    question_asker = QuestionAsker(question='', exact_answer=exact_answer, score_handler=ScoreHandler())

    # When
    is_answer_correct = question_asker.is_answer_correct(answer=given_answer)

    # Then
    assert is_answer_correct
