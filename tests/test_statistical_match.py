import pytest

from src.helpers.assert_helpers import assert_float_range, assert_numerical_range, assert_statistical_mean
from src.helpers.openai_helper import ChatGptAPI

# Parametrised test cases with questions and expected answers
@pytest.mark.parametrize("question, expected_range_float, expected_range_number, expected_mean, tolerance", [
    ("What is the value of pi to three decimal places?", (3.14, 3.142), None, None, None),
    ("What is the square root of 121. Give the exact answer alone?", None, (11, 11), None, None),
    ("What is the average of 2, 4, and 6 in one word?", None, None, 4.0, 0.1)
])

@pytest.mark.statisticalmatch
def test_statistical_validation(question, expected_range_float, expected_range_number, expected_mean, tolerance):

    response = ChatGptAPI.ask_chatgpt(question=question)

    if expected_range_float:
        assert_float_range(question, response, expected_range_float)

    if expected_range_number:
        assert_numerical_range(question, response, expected_range_number)

    if expected_mean and tolerance:
        assert_statistical_mean(question, response, expected_mean, tolerance)
