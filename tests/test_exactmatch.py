import pytest
from src.helpers.assert_helpers import assert_exact_match
from src.helpers.openai_helper import ChatGptAPI


# Parametrised test cases with questions and expected answers
@pytest.mark.parametrize("question, expected_answer", [
    ("What is the capital of France?", "The capital of France is Paris."),
    ("Who is the author of 'Hamlet'. Give the full name alone", "William Shakespeare"),
    ("What is 2 + 2 in one word?","Four.")
])


@pytest.mark.exactmatch
def test_chatgpt_exact_match(question, expected_answer):

    response = ChatGptAPI.ask_chatgpt(question=question)

    assert_exact_match(question, response, expected_answer)