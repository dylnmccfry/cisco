import requests, json, base64, sys

user = sys.argv[1]
password = sys.argv[2]
ise1 = 'SERVER1.domain.com'
endpoint_group_name = 'ENDPOINT GROUP NAME'

creds = str.encode(':'.join((user, password)))
encodedAuth = bytes.decode(base64.b64encode(creds))
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': " ".join(("Basic",encodedAuth)),
    'cache-control': "no-cache",
    }

with open("macs.txt") as file:
    macs = file.readlines()
    macs = [line.rstrip() for line in macs]

url = f"https://{ise1}:9060/ers/config/endpointgroup?filter=name.EQ.{endpoint_group_name}"
response = requests.request('GET', url, headers=headers)
endpoint_group_json = json.loads(response.text)
endpoint_group_id = (endpoint_group_json['SearchResult']['resources'][0]['id'])
#####Checks if endpoint exists, if not creates it. If it exists, it updates existing record
for host_mac in macs:
    url = f"https://{ise1}:9060/ers/config/endpoint/name/{host_mac}"
    response = requests.request('GET', url, headers=headers)
    status_code = response.status_code

    if int(status_code) != 200:
#####Creates endpoint because it doesn't already exist
        payload = """ {{
          "ERSEndPoint" : {{
            "name" : "{}",
            "description" : "Updated via API",
            "mac" : "{}",
            "groupId" : "{}",
            "staticGroupAssignment" : true
            }}
        }}""".format(host_mac,host_mac,endpoint_group_id)
        url = f"https://{ise1}:9060/ers/config/endpoint"
        response = requests.request('POST', url, headers=headers, data = payload)
        print('Creating new endpoint and assigning to group:',response.status_code)
#####Device exists in ISE database, so we must update existing device
    else:
        endpoint_id_json = json.loads(response.text)
        endpoint_id = (endpoint_id_json['ERSEndPoint']['id'])
        payload = """ {{
          "ERSEndPoint" : {{
            "name" : "{}",
            "description" : "Updated via API",
            "mac" : "{}",
            "groupId" : "{}",
            "staticGroupAssignment" : true
            }}
        }}""".format(host_mac,host_mac,endpoint_group_id)
        url = f"https://{ise1}:9060/ers/config/endpoint/{endpoint_id}"
        response = requests.request('PUT', url, headers=headers, data = payload)
        print('Updating existing endpoint:',response.status_code)
