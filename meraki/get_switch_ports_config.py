import json, operator, requests
api = open('api-key.txt').read()
payload = {}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api
}

serialList = []
serialNum = 'blank'
print('Enter a list of switch serial numbers, after the last entry press ENTER twice:')
while serialNum != '':
    serialNum = input()
    if serialNum == '':
        break
    serialList.append(serialNum.strip().replace(" ", ""))


for serials in serialList:
    url = "https://api.meraki.com/api/v1/devices/" + serials + "/switch/ports"
    response = requests.request('GET', url, headers=headers, data = payload)
    switch_port_config = json.loads(response.text)
    switch_port_config_formatted = json.dumps(switch_port_config, indent=3)
    f = open(serials + ".json", "w")
    f.write(switch_port_config_formatted)
    f.close()

print('The switch configs have been saved as [SERIAL-NUMBER].json in the same folder as this script.')
