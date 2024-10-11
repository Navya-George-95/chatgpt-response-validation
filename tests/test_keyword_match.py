import pytest

from src.helpers.assert_helpers import assert_keyword_match
from src.helpers.openai_helper import ChatGptAPI


# Parametrised test cases with questions and expected answers
@pytest.mark.parametrize("question, expected_keywords", [
    ("Name the planets in the solar system", ["Earth", "Mars", "Jupiter"]),
    ("Who wrote 'Hamlet'?", ["Shakespeare"]),
    ("What is the capital of France?", ["Paris"])
])


@pytest.mark.keywordmatch
def test_chatgpt_keyword_match(question, expected_keywords):

    response = ChatGptAPI.ask_chatgpt(question=question)

    assert_keyword_match(question, response, expected_keywords)
