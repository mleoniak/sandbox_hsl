import os
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get URL and token from environment variables
TESTMO_URL = os.getenv("TESTMO_URL", "https://hsl.testmo.net")
TESTMO_TOKEN = os.getenv(
    "TESTMO_TOKEN",
    "",
)


def create_automation_run(
    project_id, data_file="results/test-results.xml", headers=None
):

    url = f"https://hsl.testmo.net/api/v1/projects/{project_id}/automation/runs"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}

    try:
        with open(data_file, "r") as file:
            data = file.read()

        response = requests.post(
            url,
            json={"data": data, "source": "selenium", "name": "perfecto"},
            headers=headers,
        )

        if response.status_code == 200:
            logger.info("Automation run created successfully.")
        else:
            logger.error(
                f"Failed to create automation run. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error(f"Data file not found: {data_file}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


# project_id = "1"
# data_file = "results/test-results.xml"

# # Create the automation run
# run_details = create_automation_run(project_id, data_file)


def complete_automation_run(automation_run_id, base_url=TESTMO_URL, headers=None):
    """
    Complete an automation run for a given automation run ID.

    :param automation_run_id: The automation run ID to be completed
    :param base_url: The base URL of the API
    :param headers: The headers to be sent in the request
    """
    url = f"https://hsl.testmo.net/api/v1/automation/runs/{automation_run_id}/complete"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}

    try:
        with open(data_file, "r") as file:
            data = file.read()
        response = requests.post(url, headers=headers, json={"data": data})

        if response.status_code == 200:
            logger.info("Automation run completed successfully.")
        else:
            logger.error(
                f"Failed to complete automation run. Status code: {response.status_code}, Response: {response.text}"
            )
    except Exception as e:
        logger.error(f"An error occurred: {e}")


# Example usage
# Assuming you have the necessary environment variables set
project_id = "1"
data_file = "results/test-results.xml"
automation_run_id = "13"

# Create the automation run

complete_automation_run(automation_run_id)
