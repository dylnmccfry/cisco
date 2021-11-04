import json, operator, requests

api = open('api-key.txt').read()
payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api
}


serialList = []
serial = 'blank'
print('Enter a list of serials, one per line, after the last entry press ENTER twice:')
while serial != '':
    serial = input()
    if serial == '':
        break
    serialList.append(serial.strip().replace(" ", ""))

for serial in serialList:
    print('Rebooting devices...')
    url = "https://api.meraki.com/api/v1/devices/" + serial + "/reboot"
    response = requests.request('POST', url, headers=headers, data = payload)
    print(response.status_code)
    print(response.text)
