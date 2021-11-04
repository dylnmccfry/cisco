import operator, csv, meraki
organizationID = open('org-id.txt').read()

#Grabs API key from text file
api = open('api-key.txt').read()
dashboard = meraki.DashboardAPI(api)
payload = {}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api
}
#Prompt user for VLAN, Subnet Mask, and Default Gateway. Edit the DNS servers in this section as well.
print("Specify the VLAN to use, if using the Native VLAN for an Access Point, leave this blank and press enter.")
vlan = str(input() or 'null')
print("Enter the subnet mask (in this format 255.255.255.0):")
subnet_mask = str(input())
print("Enter the default gateway")
default_gateway = str(input())
dns = ["8.8.8.8","8.8.4.4"]

#Opens devices csv file and collects the IP and serials that will be used to configure each device.
with open('devices.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        ip_address = row[2]
        serial = row[0]
        wan_config={'wanEnabled': 'not configured', 'usingStaticIp': True, 'staticIp': ip_address, 'staticSubnetMask': subnet_mask, 'staticGatewayIp': default_gateway, 'staticDns': dns}
#Checks if VLAN is null, which is default value. If so, the APs should be using the native VLAN on the switch port. Switches should NOT have this set to null, only APs on native VLAN.
        if vlan != 'null':
            wan_config['vlan'] = int(vlan)
        else:
            wan_config['vlan'] = None
        wan1=wan_config
        response = dashboard.devices.updateDeviceManagementInterface(
            serial,
            wan1=wan_config
        )
        print(response)
