import json, operator, requests
my_string = 'None'
print('Enter the serial of a switch to clone port configurations FROM: ')
switch_serial_cf = input()
print('Enter the serial of a switch to clone port configurations TO: ')
switch_serial_ct = input()
url = "https://api.meraki.com/api/v1/devices/" + switch_serial_cf + "/switch/ports"
api = open('api-key.txt').read()
payload = {}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api
}

response = requests.request('GET', url, headers=headers, data = payload)
switch_port_config = json.loads(response.text)

total_ports = len(switch_port_config)
print(str(len(switch_port_config)) + ' Ports on this switch.')
for port_id in switch_port_config:
    if str(port_id["voiceVlan"]) == 'None':
        del port_id['voiceVlan']

    if str(port_id["portScheduleId"]) == 'None':
        del port_id["portScheduleId"]

    url = "https://api.meraki.com/api/v1/devices/" + switch_serial_ct + "/switch/ports/" + port_id["portId"]
    payload = json.dumps(port_id, indent=4)
    response = requests.request('PUT', url, headers=headers, data = payload)
    print('Configuring port ', str(port_id["portId"]), 'HTTP CODE: ', response.status_code, end="\r", flush=True)
