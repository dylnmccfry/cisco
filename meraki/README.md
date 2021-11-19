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
