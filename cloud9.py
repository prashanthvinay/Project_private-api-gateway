import requests

API_URL = "https://<API Id>-<VPC Endpoint ID>.execute-api.us-east-1.amazonaws.com/<STAGE>"

try:
    response = requests.get(API_URL)
    print(response.json())
except:
    print('Execution Timed Out!')
