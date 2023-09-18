import meraki
import time
import csv
print("Specify the VLAN to use, if using the Native VLAN for an Access Point, leave this blank and press enter.")
vlan = (input() or None)
with open('api-key.txt', "r") as file:
    api_key = file.read()
dashboard = meraki.DashboardAPI(api_key)

device_serial_list = []
##Gets list for serials 
with open('devices.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
#Read csv file by rows, first value is the serial number
        device_serial = row[0]
#Updates the serial list
        device_serial_list.append(device_serial)

# Iterate through list of serial numbers and change to use DHCP and specified VLAN
for serial in device_serial_list:
    response = dashboard.devices.getDeviceManagementInterface(
        serial
    )
    switch_management_info = response
    response = dashboard.devices.updateDeviceManagementInterface(
    serial, 
    wan1={'usingStaticIp': False, 'vlan': vlan}
        )
    print(response)
    time.sleep(1)