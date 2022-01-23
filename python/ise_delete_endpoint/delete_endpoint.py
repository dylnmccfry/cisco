import requests, json, base64, sys, getpass

user = input("Username: ")
password = getpass.getpass()
ise1 = 'SERVER1.domain.com'

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
#Get endpoint id used to delete endpoint from ISE
for host_mac in macs:
    url = f"https://{ise1}:9060/ers/config/endpoint/name/{host_mac}"
    response = requests.request('GET', url, headers=headers)
#If endpoint is not found 404 handling
    if response.status_code == 404:
        print(host_mac,'was not found')
#If endpoint is found, use it's ID to delete it
    else:
        endpoint_json = json.loads(response.text)
        endpoint_id = (endpoint_json['ERSEndPoint']['id'])
        url = f"https://{ise1}:9060/ers/config/endpoint/{endpoint_id}"
        response = requests.delete(url, headers=headers)
        print('Deleting endpoint',response.status_code)
