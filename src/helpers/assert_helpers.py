import logging
from src.helpers.computation_helpers import compute_similarity, keyword_matching, extract_float, extract_number, \
    calculate_gpt_models_cosine_similarity

logging.basicConfig(level=logging.INFO)

def assert_exact_match(question, response, expected_answer):
    logging.info("\n")
    logging.info("***** Test for exact match *****")
    logging.info(f"Input prompt : {question}")
    logging.info(f"Received Response: {response}")
    logging.info(f"Expected Answer: {expected_answer}")
    logging.info(f"Check if the response exactly matches the expected answer.")
    assert response == expected_answer, logging.error(
        f"Test is failed. Expected {expected_answer}, but got {response}") or f"Test is failed. Expected {expected_answer}, but got {response}"
    logging.info("Test is passed. Response exactly matches with expected answer.")

def assert_similarity(question, response, expected_answer, threshold=0.85):
    logging.info("\n")
    logging.info("***** Test for similarity match *****")
    logging.info(f"Input prompt : {question}")
    logging.info(f"Received Response: {response}")
    logging.info(f"Expected Answer: {expected_answer}, Threshold: {threshold}")
    logging.info("Check if the similarity between response and expected answer exceeds specified threshold.")
    similarity = compute_similarity(response, expected_answer)
    logging.info(f"Computed similarity : {similarity}")
    assert similarity >= threshold, logging.error(
        f"Test is failed. Expected minimum {threshold} similarity, but got only {similarity}") or f"Test is failed. Expected minimum {threshold} similarity, but got only {similarity}"
    logging.info(f"Test is passed. Similarity is above specified threshold of {threshold}.")


def assert_keyword_match(question, response, expected_keywords):
    logging.info("\n")
    logging.info("***** Test for Keyword match *****")
    logging.info(f"Input prompt : {question}")
    logging.info(f"Received Response: {response}")
    logging.info(f"Expected Keywords: {expected_keywords}")
    logging.info("Check if the response contains all expected keywords.")
    assert keyword_matching(response, expected_keywords),logging.error(
        f"Test is failed. Expected keywords not present in response") or f"Test is failed. Expected keywords not present in response"
    logging.info(f"Test is passed. Expected keywords present in response")


def assert_float_range(question, response, expected_range):
    logging.info("\n")
    logging.info("***** Test for Statistical match *****")
    logging.info(f"Input prompt : {question}")
    logging.info(f"Received Response: {response}")
    logging.info(f"Expected Range: {expected_range}")
    logging.info("Check if the response is within a specified float range.")
    extracted_value = extract_float(response)
    assert extracted_value is not None, logging.error(f"No float found in response: {response}") or "No float found in response: {response}"
    assert expected_range[0] <= extracted_value <= expected_range[1], logging.error(
        f"Test is failed. Extracted value {extracted_value} not in expected float range {expected_range}") or f"Test is failed. Extracted value {extracted_value} not in expected float range {expected_range}"
    logging.info(f"Test is passed. Extracted value {extracted_value} with in expected float range {expected_range}")


def assert_numerical_range(question, response, expected_range):
    logging.info("\n")
    logging.info("***** Test for Statistical match *****")
    logging.info(f"Input prompt : {question}")
    logging.info(f"Received Response: {response}")
    logging.info(f"Expected Range: {expected_range}")
    logging.info("Check if the response is within a specified numerical range.")
    extracted_value = extract_number(response)
    assert extracted_value is not None, logging.error(
        f"No number found in response: {response}") or "No number found in response: {response}"
    assert expected_range[0] <= extracted_value <= expected_range[1], logging.error(
        f"Test is failed. Extracted value {extracted_value} not in expected numerical range {expected_range}") or f"Test is failed. Extracted value {extracted_value} not in expected numerical range {expected_range}"
    logging.info(f"Test is passed. Extracted value {extracted_value} with in expected numerical range {expected_range}")


def assert_statistical_mean(question, response, expected_mean, tolerance):
    logging.info("\n")
    logging.info("***** Test for Statistical match *****")
    logging.info(f"Input prompt : {question}")
    logging.info(f"Received Response: {response}")
    logging.info(f"Expected Mean: {expected_mean} , Expected Tolerance: {tolerance}")
    logging.info("Check if the response matches a statistical mean with a tolerance.")
    extracted_mean = extract_number(response.strip('.'))
    extracted_tolerance = abs(extracted_mean - expected_mean)
    assert extracted_mean is not None, logging.error(
        f"No float/number found in response: {response}") or "No float/number found in response: {response}"
    assert  extracted_tolerance <= tolerance, logging.error(
        f"Test is failed. Extracted value {extracted_mean} not within tolerance {tolerance} of mean {expected_mean}") or f"Test is failed. Extracted value {extracted_mean} not within tolerance {tolerance} of mean {expected_mean}"
    logging.info(f"Test is passed. Extracted mean {extracted_mean} within expected mean {expected_mean} and tolerance {tolerance} ")


def assert_cosine_similarity(question, model1_response, model2_response, threshold=0.85):
    logging.info("\n")
    logging.info("***** Test for comparing different gpt models *****")
    logging.info(f"Input prompt : {question}")
    logging.info(f"Received Response of Model 1: {model1_response}")
    logging.info(f"Received Response of Model 2: {model2_response}")
    logging.info(f"Expected Threshold: {threshold}")
    logging.info(f"Check if the similarity between two models is above the threshold: {threshold}.")
    similarity = calculate_gpt_models_cosine_similarity(model1_response,model2_response)
    logging.info(f"Computed similarity : {similarity}")
    assert similarity >= threshold, logging.error(
        f"Test is failed. Expected minimum {threshold} similarity, but got only {similarity}") or f"Test is failed. Expected minimum {threshold} similarity, but got only {similarity}"
    logging.info(f"Test is passed. Similarity is above specified threshold of {threshold}.")
