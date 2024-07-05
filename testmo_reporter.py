import requests
import json
import os

TESTMO_API_URL = os.getenv("TESTMO_API_URL")
API_KEY = os.getenv("TESTMO_API_KEY")


def create_test_run(project_id, name):
    url = f"{TESTMO_API_URL}/runs"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"project_id": project_id, "name": name}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


def add_test_result(run_id, case_id, status, comment=""):
    url = f"{TESTMO_API_URL}/runs/{run_id}/results"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"case_id": case_id, "status": status, "comment": comment}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()
