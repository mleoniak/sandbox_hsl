import requests
import os
import logging
import xml.etree.ElementTree as ET


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get URL and token from environment variables
TESTMO_URL = os.getenv("TESTMO_URL")
TESTMO_TOKEN = os.getenv("TESTMO_TOKEN")

# Define the XML data
xml_file_path = 'results/test-results.xml'
# Read the XML data from the file
with open(xml_file_path, 'r') as file:
    xml_data = file.read()

# Parse the XML data
tree = ET.fromstring(xml_data)

# Find all testcase elements within the testsuite
testcases = tree.findall('.//testcase')
testsuite = tree.findall('.//testsuite')

# Get the second testcase element (index 1)
# second_testcase = testcases[1]

# Extract attributes from the second testcase
# classname = second_testcase.get('classname')
# name = second_testcase.get('name')
# time = second_testcase.get('time')

# # Extract the time attribute from the first testcase
# # print(time)
# # print(name)
# # print(len(testcases))

# for testcase in range(len(testcases)):
#     classname = testcases[testcase].get('classname')
#     print(classname.replace('tests.', ''))

####################################################################

elapsed_observed = float(testsuite[0].get('time'))
elapsed_observed = int(elapsed_observed * 1000000)

{
                        "key": "idk",
                        "name": "tests.test_01_nav_visibility",
                        "status": "passed",
                        "folder": "best",
                        "elapsed": 100000000,
}


def create_automation_run(project_id, source, name, headers=None):
    """
    Creates a new automation run in a target project in preparation for adding threads and test results.
    """
    url = f"{TESTMO_URL}/api/v1/projects/{project_id}/automation/runs"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={"source": source, "name": name},
            headers=headers,
        )
        if response.status_code == 201:
            logger.info(
                f"Automation run created successfully. Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error(
                f"Failed to create automation run. Status code: {response.status_code}, Response: {response.text}"
            )
        return response.json()
    except FileNotFoundError:
        logger.error("Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def add_threads_to_automation_run(automation_run_id, headers=None):
    """
    Creates a new thread in an automation run in preparation for adding test results.
    """
    url = f"{TESTMO_URL}/api/v1/automation/runs/{automation_run_id}/threads"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={"elapsed_observed": 555000000, "elapsed_computed": 111000000},
            headers=headers,
        )
        if response.status_code == 201:
            logger.info(
                f"Threads added to automation run successfully. Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error(
                f"Failed to add threads to automation run. Status code: {response.status_code}, Response: {response.text}"
            )
        return response.json()
    except FileNotFoundError:
        logger.error("Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def append_test_results_to_thread(thread_id, headers=None):

    def add_test(json, key, name, status, folder, elapsed):
        new_test = {
            "key": key,
            "name": name,
            "status": status,
            "folder": folder,
            "elapsed": elapsed
         }
        json["tests"].append(new_test)

    json_payload = {"tests": []}

    # Add your test results here dynamically
    add_test(json_payload, "test1", "tests12312312", "passed", "best", 100000000)
    add_test(json_payload, "test2", "66666", "passed", "best", 100000000)
    # You can continue to add more test results as needed

    # for testcase in testcases:
    #     add_test(json_payload, testcase["key"], testcase["name"], testcase["status"], testcase["folder"], testcase["elapsed"])


    """
    Append test results to an existing thread in an automation run.

    :param thread_id: The ID of the thread to which test results will be appended.
    :param headers: Optional headers for the request. If not provided, default headers with authorization token will be used.
    """
    url = f"{TESTMO_URL}/api/v1/automation/runs/threads/{thread_id}/append"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json=json_payload,
            headers=headers
        )
        if response.status_code == 204:
            logger.info(
                f"Test results appended to thread successfully. Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error(
                f"Failed to append test results to thread. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error("Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def complete_automation_thread(thread_id, headers=None):
    """
    Mark a thread in an automation run as complete.

    :param thread_id: The ID of the thread to mark as complete.
    :param headers: Optional headers for the request. If not provided, default headers with authorization token will be used.
    """
    url = f"{TESTMO_URL}/api/v1/automation/runs/threads/{thread_id}/complete"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={"elapsed_observed": elapsed_observed, "elapsed_computed": 777000000},
            headers=headers,
        )
        if response.status_code == 204:
            logger.info(
                f"Thread marked as complete successfully. Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error(
                f"Failed to mark thread as complete. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error("Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def complete_automation_run(automation_run_id, headers=None):
    """
    Mark an entire automation run as complete.

    :param automation_run_id: The ID of the automation run to mark as complete.
    :param headers: Optional headers for the request. If not provided, default headers with authorization token will be used.
    """
    url = f"{TESTMO_URL}/api/v1/automation/runs/{automation_run_id}/complete"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={},
            headers=headers,
        )
        if response.status_code == 204:
            logger.info(
                f"Automation run marked as complete successfully. Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error(
                f"Failed to mark automation run as complete. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error("Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    project_id = 1
    source = "VSC"
    name = "Test Automation Run"

    new_automation_run = create_automation_run(project_id, source, name)
    print(new_automation_run)

    automation_run_id = new_automation_run['id']

    new_thread = add_threads_to_automation_run(automation_run_id)
    print(new_thread)
    thread_id = new_thread["id"]
    
    append_test_results_to_thread(thread_id)

    complete_automation_thread(thread_id)

    complete_automation_run(automation_run_id)
