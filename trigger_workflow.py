# trigger_workflow.py
import requests
import os

OWNER = "MelleAI"
REPO = "auto-reddit-shorts"
WORKFLOW_ID = "daily.yml"
BRANCH = "main"

TOKEN = os.getenv("GH_PAT")

url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}/dispatches"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

data = {"ref": BRANCH}

resp = requests.post(url, headers=headers, json=data)

if resp.status_code == 204:
    print("Workflow triggered successfully!")
else:
    print(f"Failed to trigger workflow: {resp.status_code}")
    print(resp.text)
