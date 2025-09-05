import requests
import urllib3

# WARNING: Disabling SSL verification is insecure and should only be used for testing!
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
url = "https://your-api-endpoint.com/path"  # Replace with your URL
token = "your_token_here"                   # Replace with your token

# Payload
payload = {"run-playbook": True}

# Headers
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Send POST request (ignoring SSL certs)
response = requests.post(url, json=payload, headers=headers, verify=False)

# Print response
print("Status Code:", response.status_code)
print("Response Body:", response.text)
