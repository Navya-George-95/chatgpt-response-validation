# Automate ChatGpt Response Validation #

This repository contains a Python-based automation framework using Pytest to validate responses from ChatGPT (OpenAI API). The framework allows for validations like exact match, keyword-based match, similarity match, comparing different gpt models and statistical validation of responses from the OpenAI GPT models.

## Prerequisites
Before you begin, ensure you have the following installed:

Python 3.10 or later 

pip (Python package manager)

An OpenAI API key (You can get this from OpenAI's API platform)

Allure command-line tool for report generation (optional for enhanced reporting)

### Installation

1. Clone the repository
    ```bash
    git clone https://github.com/Navya-George-95/chatgpt-response-validation.git
    
   cd chatgpt-response-validation
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
    python -m venv .venv
    
    source .venv/bin/activate    # On Windows: .venv\Scripts\activate
   ```

3. Install project dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Set your OpenAI API key in config.toml file in the below format:
   ```bash
   [openai]
   
   openai_key = "your-api-key-here"
   ```

## Running Tests

To run the entire suite, use the following command:

   ```bash
   pytest
   ```

## Project Structure

Purpose of key folders in project is below:

- `src/constants`: Constant values required across tests.
- `src/helpers`: Common utilities and assertions required across tests.
- `target` : Reports, logs and other results
- `tests`: Contains test modules organized by functionality.

## Allure Reporting
This framework is integrated with Allure for generating beautiful test reports which will displayed in your browser automatically once the test execution is complete.

## Additional Notes
Pytest is used as the test framework, and Allure is integrated for reporting.
The framework is modular, with utilities and helper functions separated for better maintainability.

## Who do I talk to? ###

* Navya George M