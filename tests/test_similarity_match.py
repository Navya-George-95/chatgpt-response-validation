import pytest

from src.helpers.assert_helpers import assert_similarity
from src.helpers.openai_helper import ChatGptAPI


# Parametrised test cases with questions and expected answers
@pytest.mark.parametrize("question, expected_answer", [
    ("What is the capital of France?", "Capital is Paris"),
    ("What is 2 + 2", "The result of What is 2 + 2 is 4."),
    ("Who wrote 'Hamlet'", "Hamlet was authored by William Shakespeare, one of the most famous playwrights in history. "
                           "It is a tragedy that was likely composed between 1599 and 1601.")
])


@pytest.mark.similaritymatch
def test_chatgpt_response_similarity(question, expected_answer):

    response = ChatGptAPI.ask_chatgpt(question=question)

    assert_similarity(question, response, expected_answer)
