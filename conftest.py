import logging
import shutil, sys, time, pytest, openai, toml, os, subprocess

# Open allure results in browser after test execution is complete
def pytest_sessionfinish(session, exitstatus):

    allure_results_dir = os.path.join(os.getcwd(), 'target', 'allure-results')
    allure_report_dir = os.path.join(os.getcwd(), 'target', 'allure-report')

    # Generate the Allure report from the results
    subprocess.run(f"allure generate {allure_results_dir} -o {allure_report_dir} --clean", shell=True)

    # Start the Allure server in a new process (non-blocking)
    server_process = subprocess.Popen(f"allure open {allure_report_dir}", shell=True)

    # Wait for 5 seconds to ensure the report is opened
    time.sleep(5)

    # Kill the server process (this will stop the web server)
    server_process.terminate()

    # Exit the Python script and stop the process
    sys.exit(0)

@pytest.fixture(scope="session", autouse=True)
def openai_setup():
    """
    Pytest fixture to set up OpenAI API key from the config.toml file.
    It runs automatically for all tests in the session and aborts immediately on any error.
    """
    config_path = 'config.toml'

    # Check if the config file exists
    if not os.path.exists(config_path):
        pytest.exit(f"Configuration file '{config_path}' not found. Aborting the test session.")

    # Load the config file, immediately exit when any error encounters
    try:
        with open(config_path, 'r') as f:
            config = toml.load(f)
    except toml.TomlDecodeError as e:
        pytest.exit(f"Error decoding TOML file: {e}. Aborting the test session.")

    # Set the OpenAI API key
    if 'openai' in config and 'openai_key' in config['openai']:
        openai.api_key = config['openai']['openai_key']
    else:
        pytest.exit("API key not found in the 'openai' section of the config file. Aborting the test session.")
