import pytest

from src.helpers.assert_helpers import assert_cosine_similarity
from src.helpers.openai_helper import ChatGptAPI
from src.constants.constants import MODEL2

# Parametrised test cases with questions and expected answers
@pytest.mark.parametrize("question", [
    "Explain the process of photosynthesis in simple terms."
])


@pytest.mark.comparegpts
def test_chatgpt_keyword_match(question):
    # GPT-4 response
    gpt4_output = ChatGptAPI.ask_chatgpt(question=question,model=MODEL2)

    # GPT-4o-mini response
    gpt40mini_output = ChatGptAPI.ask_chatgpt(question=question)

    assert_cosine_similarity(question, gpt4_output, gpt40mini_output)