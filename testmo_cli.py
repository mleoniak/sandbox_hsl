import requests
import os
import logging
import xml.etree.ElementTree as ET
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for XML file path
XML_FILE_PATH = 'results/test-results.xml'

# Retrieve environment variables
TESTMO_URL = os.getenv("TESTMO_URL")
TESTMO_TOKEN = os.getenv("TESTMO_TOKEN")

def load_xml_data(file_path):
    """
    Load and parse XML data from a file.
    """
    try:
        with open(file_path, 'r') as file:
            xml_data = file.read()
        return ET.fromstring(xml_data)
    except FileNotFoundError:
        logger.error(f"XML file not found: {file_path}")
    except ET.ParseError:
        logger.error(f"Failed to parse XML file: {file_path}")

def extract_testcases_and_time(tree):
    """
    Extract test cases and elapsed time from the XML tree.
    """
    try:
        testcases = tree.findall('.//testcase')
        testsuite = tree.findall('.//testsuite')
        elapsed_observed = float(testsuite[0].get('time'))
        elapsed_observed = int(elapsed_observed * 1000000)
        return testcases, elapsed_observed
    except (IndexError, AttributeError) as e:
        logger.error(f"Failed to extract data from XML: {e}")
        return [], 0

def create_automation_run(project_id, source, name, headers=None):
    """
    Creates a new automation run in a target project in preparation for adding threads and test results.
    """
    url = f"{TESTMO_URL}/api/v1/projects/{project_id}/automation/runs"
    headers = headers or {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    payload = {"source": source, "name": name}
    
    return make_post_request(url, payload, headers, "create automation run")

def add_threads_to_automation_run(automation_run_id, headers=None):
    """
    Creates a new thread in an automation run in preparation for adding test results.
    """
    url = f"{TESTMO_URL}/api/v1/automation/runs/{automation_run_id}/threads"
    headers = headers or {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    payload = {"elapsed_observed": 0, "elapsed_computed": 0}
    
    return make_post_request(url, payload, headers, "add threads to automation run")

def append_test_results_to_thread(thread_id, testcases, headers=None):
    """
    Appends test results to an existing thread in an automation run.
    """
    headers = headers or {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    url = f"{TESTMO_URL}/api/v1/automation/runs/threads/{thread_id}/append"
    json_payload = {"tests": []}
    
    for testcase in testcases:
        name = testcase.get("name")
        folder = testcase.get("classname").replace("tests.", "")
        time = int(float(testcase.get("time")) * 1000000)
        if testcase.find("error") is not None or testcase.find("failure") is not None:
            status = "failed"
        else:
            status = "passed"
        
        json_payload["tests"].append({
            "key": "default",
            "name": name,
            "status": status,
            "folder": folder,
            "elapsed": time
        })

    make_post_request(url, json_payload, headers, "append test results to thread")

def complete_automation_thread(thread_id, elapsed_observed, headers=None):
    """
    Mark a thread in an automation run as complete.
    """
    url = f"{TESTMO_URL}/api/v1/automation/runs/threads/{thread_id}/complete"
    headers = headers or {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    payload = {"elapsed_observed": elapsed_observed, "elapsed_computed": 777000000}
    
    make_post_request(url, payload, headers, "complete automation thread")

def complete_automation_run(automation_run_id, headers=None):
    """
    Mark an entire automation run as complete.
    """
    url = f"{TESTMO_URL}/api/v1/automation/runs/{automation_run_id}/complete"
    headers = headers or {"Authorization": f"Bearer {TESTMO_TOKEN}"}
    
    make_post_request(url, {}, headers, "complete automation run")

def make_post_request(url, payload, headers, action):
    """
    Makes a POST request and handles common response scenarios.
    """
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 201 or response.status_code == 204:
            logger.info(f"{action.capitalize()} successfully. Status code: {response.status_code}")
        else:
            logger.error(f"Failed to {action}. Status code: {response.status_code}, Response: {response.text}")
        return response.json() if response.content else {}
    except requests.RequestException as e:
        logger.error(f"An error occurred during {action}: {e}")

def testmo_run(source, name, project_id=1):
    """
    Orchestrates the automation run process in Testmo.
    """
    xml_tree = load_xml_data(XML_FILE_PATH)
    if xml_tree is None:
        return

    testcases, elapsed_observed = extract_testcases_and_time(xml_tree)
    if not testcases:
        return
    
    new_automation_run = create_automation_run(project_id, source, name)
    automation_run_id = new_automation_run.get('id')
    if not automation_run_id:
        return

    new_thread = add_threads_to_automation_run(automation_run_id)
    thread_id = new_thread.get("id")
    if not thread_id:
        return
    
    append_test_results_to_thread(thread_id, testcases)
    complete_automation_thread(thread_id, elapsed_observed)
    complete_automation_run(automation_run_id)

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Run Testmo automation")
    parser.add_argument('source', type=str, help='Source for the automation run')
    parser.add_argument('name', type=str, help='Name for the automation run')
    parser.add_argument('--project_id', type=int, default=1, help='Project ID for the automation run')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    testmo_run(args.source, args.name, args.project_id)
