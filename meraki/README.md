# Usage
This repo includes a few scripts to speed up deployment of a new Meraki location. This focuses on MR and MS devices.
## Installation
You will need the [meraki](https://github.com/meraki/dashboard-api-python) python library. You will also need [tkinter](https://docs.python.org/3/library/tkinter.html)
## Usage
Place your api key in the folder these scripts are in. The filename should be api-key.txt
Place the org ID in the folder these scripts are in. The filename should be org-id.txt

## get_switch_ports_config.py
This will copy the port configs into json files, in the same folder this script is run from. The filenames will be the serialnumber .json

## set_IP.py
This will configure static IP addresses on MR or MS devices. The default DNS servers are 8.8.8.8 and 8.8.4.4
This uses the information in devices.csv to assign the IP address and will prompt you for subnet mask, VLAN, and gateway.  

## get_network_id.py
This will provide the network ID for a specified network, using a GUI.

## reboot.py
This will reboot the devices.

## claim_device_rename.py
This will claim devices to an org & network, and rename them using the devices.csv values.

## clone_switch_ports_config.py
This will clone switch port configs from a switch to another switch. It will prompt for a serial number to copy FROM and a serial number to copy TO.

## rename_networks.py
This will rename networks by moving the second and third index in a string that was split into a list, and moving that to the end of the string.

## set_managment_interface_to_dhcp_no_check.py
This will read the serial numbers from the devices.csv file and update the management interface to use the VLAN you specify. For example:

```
Specify the VLAN to use, if using the Native VLAN for an Access Point, leave this blank and press enter.
30
2029-09-18 10:53:16       meraki:     INFO > devices, updateDeviceManagementInterface - 200 OK
{'wan1': {'usingStaticIp': False, 'vlan': 30}}
```