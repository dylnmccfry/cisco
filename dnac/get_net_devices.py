import requests
import json
import urllib3
import csv
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
json_data = json.loads(response.text)
token = str(json_data["Token"])


url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'X-Auth-Token': token
}
# Prints the hostname, IP, and platform
response = requests.request("GET", url, headers=headers, data=payload, verify=False)
json_data = json.loads(response.text)
for device in json_data["response"]:
    print(device["hostname"],device["managementIpAddress"],device["platformId"])