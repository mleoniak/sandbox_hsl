# import requests
# import os
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Get URL and token from environment variables
# TESTMO_URL = os.getenv("TESTMO_URL")
# TESTMO_TOKEN = os.getenv("TESTMO_TOKEN")


# def automations_runs(project_id, headers=None):

#     # actual_runs = requests.get(f"{TESTMO_URL}/api/v1/projects/{project_id}/automation/runs",
# headers={"Authorization": f"Bearer {TESTMO_TOKEN}"})

#     # print(actual_runs.json())

#     url = f"{TESTMO_URL}/api/v1/projects/{project_id}/automation/runs"
#     if headers is None:
#         headers = {"Authorization": f"Bearer {TESTMO_TOKEN}"}

#     try:
#         response = requests.post(
#             url,
#             json={"source": "selenium", "name": "perfecto"},
#             headers=headers,
#         )

#         if response.status_code == 201:
#             logger.info(
#                 f"Automation run created successfully.Status code: {response.status_code}, Response: {response.text}"
#             )
#         else:
#             logger.error(
#                 f"Failed to create automation run. Status code: {response.status_code}, Response: {response.text}"
#             )

#     except FileNotFoundError:
#         logger.error(f"Data file not found")
#     except Exception as e:
#         logger.error(f"An error occurred: {e}")


# project_id = "1"
# automations_runs(project_id)
