import requests
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get URL and token from environment variables
TESTMO_URL = os.getenv("TESTMO_URL")
TESTMO_TOKEN = os.getenv("TESTMO_TOKEN")


def create_new_automation_run(project_id, headers=None):

    # actual_runs = requests.get(f"{TESTMO_URL}/api/v1/projects/{project_id}/automation/runs",
    # headers={"Authorization": f"Bearer {TESTMO_TOKEN}"})

    # print(actual_runs.json())

    url = f"{TESTMO_URL}/api/v1/projects/{project_id}/automation/runs"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={"source": "selenium", "name": "perfecto"},
            headers=headers,
        )
        if response.status_code == 201:
            logger.info(
                f"Automation run created successfully.Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error
            (
                f"Failed to create automation run. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error(f"Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    return response.json()

# project_id = "1"
# new_id = create_new_automation_run(project_id)
# print(new_id)

# automation_run_id = new_id["id"]

def add_threads_to_new_automation_run(automation_run_id, headers=None):
    pass
    url = f"{TESTMO_URL}/api/v1/automation/runs/{automation_run_id}/threads"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={"source": "selenium", "name": "perfecto"},
            headers=headers,
        )
        if response.status_code == 201:
            logger.info(
                f"Threads automation run created successfully.Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error
            (
                f"Failed to create threads automation run. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error(f"Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    return response.json()

# new_thread_id = add_threads_to_new_automation_run()
# print(new_thread_id)

# thread_id = new_thread_id["id"]


def append_tests_result_to_thread(thread_id, headers=None):

    url = f"{TESTMO_URL}/api/v1/automation/runs/threads/{thread_id}/append"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={
                "tests": [
                    {
                        "key": "selenium",
                        "name": "tests.test_01_nav_visibility",
                        "status": "passed",
                        "folder": "best",
                    }
                ],
            },
            headers=headers
        )
        if response.status_code == 201:
            logger.info(
                f"Append to thread automation run successfully.Status code: {response.status_code}, Response:"
            )
        else:
            logger.error
            (
                f"Failed to append thread automation run. Status code: {response.status_code}, Response: "
            )
    except FileNotFoundError:
        logger.error(f"Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
  


# automation_run_thread_id = append_tests_result_to_thread()
# print(automation_run_thread_id)


def complete_automation_run(thread_id, headers=None):
    pass
    url = f"{TESTMO_URL}/api/v1/automation/runs/threads/{thread_id}/complete"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={},
            headers=headers,
        )
        if response.status_code == 201:
            logger.info(
                f"Complete thread automation run created successfully.Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error
            (
                f"Failed to complite thread automation run. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error(f"Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# finish = complete_automation_run()
# print(finish)

def automation_run_complite(automation_run_to_complite, headers=None):
    pass
    url = f"{TESTMO_URL}/api/v1/automation/runs/{automation_run_to_complite}/complete"
    if headers is None:
        headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    try:
        response = requests.post(
            url,
            json={},
            headers=headers,
        )
        if response.status_code == 201:
            logger.info(
                f"Complete thread automation run created successfully.Status code: {response.status_code}, Response: {response.text}"
            )
        else:
            logger.error
            (
                f"Failed to complite thread automation run. Status code: {response.status_code}, Response: {response.text}"
            )
    except FileNotFoundError:
        logger.error(f"Data file not found")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# finish_run = automation_run_complite()
# print(finish_run)



# start session 
project_id = 1

new_id = create_new_automation_run(project_id)
print(new_id)
automation_run_id = new_id["id"]

# add thread to running test
new_thread_id = add_threads_to_new_automation_run(automation_run_id)
print(new_thread_id)
thread_id = new_thread_id["id"]

# append tests result from report
append_tests_result_to_thread(thread_id)

# complete thread
complete_automation_run(thread_id)

#complete session
automation_run_to_complite = automation_run_id
automation_run_complite(automation_run_to_complite)