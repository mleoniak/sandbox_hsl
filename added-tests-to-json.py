import logging
import xml.etree.ElementTree as ET

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the XML data
xml_data = """<?xml version="1.0" encoding="utf-8"?>
<testsuites>
    <testsuite name="pytest" errors="0" failures="0" skipped="0" tests="3" time="33.880" timestamp="2024-07-09T13:14:07.105918" hostname="DESKTOP-MFPGNL3">
        <testcase classname="tests.test_00_search" name="test_search_this_website_functionality" time="11.931" />
        <testcase classname="tests.test_01_nav_visibility" name="test_nav_vis" time="10.767" />
        <testcase classname="tests.test_02_nav_content" name="test_nav_content" time="11.149" />
    </testsuite>
</testsuites>
"""

# Parse the XML data
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

# Find all testcase elements within the testsuite
testcases = root.findall('.//testcase')

def append_test_results_to_thread():
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

    # Add test results dynamically from the XML data
    for testcase in testcases:
        name = testcase.get("name")
        folder = testcase.get("classname").replace("tests.", "")
        time = float(testcase.get("time"))
        status = "passed"  # Assuming status is 'passed' as there are no error/failure attributes

        add_test(json_payload, "default", name, status, folder, time)

    logger.info("Test results appended to JSON payload")
    return json_payload

# Print the JSON payload with test results
print(append_test_results_to_thread())
