import pandas as pd
from netmiko import Netmiko
from getpass import getpass
# Cisco switch connection details
df = pd.DataFrame(columns=['MAC', 'Interface', 'VLAN'])
df.to_excel('mac_table.xlsx')
switches = ['10.10.10.10', '10.10.10.101', '10.10.10.102', '10.10.10.103', '10.10.10.104']
username = input('Username:')
password = getpass()
for switch in switches:
    try:
        # Connect to the Cisco switch via Telnet
        
        net_connect = Netmiko(host=switch, username=username, password=password, device_type='cisco_ios_telnet')
        print('connecting to', switch)
        # Send the command to retrieve the MAC address table
        mac_command = 'show mac address-table dynamic'
        output = net_connect.send_command(mac_command, use_textfsm=True)

        # Parse the MAC address table output to extract MAC addresses, ports, and VLANs
        mac_addresses = []
        ports = []
        vlans = []
        mac_data = {'mac': [entry['destination_address'] for entry in output],
                'interface': [entry['destination_port'] for entry in output],
                'vlan': [entry['vlan'] for entry in output]
                }
        mac_addresses = mac_data['mac']
        ports_list = mac_data['interface']
        for sublist in ports_list:
            for item in sublist:
                ports.append(item)
        vlans = mac_data['vlan']
        # Send the command to retrieve the CDP neighbors
        cdp_table = net_connect.send_command("sh cdp neighbors detail", use_textfsm=True)
        cdp_data = {
        'local_interface': [entry['local_port'] for entry in cdp_table]
        }
        # Parse the CDP neighbors output to extract interfaces with CDP neighbors
        cdp_interfaces_list = cdp_data['local_interface']
        cdp_interfaces = [string.replace(' ','') for string in cdp_interfaces_list]
        cdp_interfaces = [string.replace('GigabitEthernet','Gi') for string in cdp_interfaces]
        cdp_interfaces = [string.replace('FastEthernet','Fa') for string in cdp_interfaces]
        # Disconnect from the Cisco switch
        net_connect.disconnect()
        # Filter out MAC addresses found on interfaces with CDP neighbors
        filtered_mac_addresses = []
        filtered_ports = []
        filtered_vlans = []
        for mac_address, port, vlan in zip(mac_addresses, ports, vlans):
            if port not in cdp_interfaces and ports.count(port) > 1:
                filtered_mac_addresses.append(mac_address)
                filtered_ports.append(port)
                filtered_vlans.append(vlan)

        # Create a DataFrame to store the filtered MAC addresses, ports, and VLANs
        df = pd.DataFrame({
            'Switch': switch,
            'Port': filtered_ports,
            'MAC Address': filtered_mac_addresses,
            'VLAN': filtered_vlans
        })

        # Save the DataFrame to an Excel file
        with pd.ExcelWriter('mac_table.xlsx', engine='openpyxl', mode='a') as writer:
            df.to_excel(writer, index=False, sheet_name=switch)

        
    except:
# Connect to the Cisco switch via SSH
        net_connect = Netmiko(host=switch, username=username, password=password, device_type='cisco_ios')
        print('connecting to', switch)
        # Send the command to retrieve the MAC address table
        mac_command = 'show mac address-table dynamic'
        output = net_connect.send_command(mac_command, use_textfsm=True)

        # Parse the MAC address table output to extract MAC addresses, ports, and VLANs
        mac_addresses = []
        ports = []
        vlans = []
        mac_data = {'mac': [entry['destination_address'] for entry in output],
                'interface': [entry['destination_port'] for entry in output],
                'vlan': [entry['vlan'] for entry in output]
                }

        mac_addresses = mac_data['mac']
        ports_list = mac_data['interface']
        for sublist in ports_list:
            for item in sublist:
                ports.append(item)
        vlans = mac_data['vlan']

        # Send the command to retrieve the CDP neighbors
        cdp_table = net_connect.send_command("sh cdp neighbors detail", use_textfsm=True)
        cdp_data = {
        'local_interface': [entry['local_port'] for entry in cdp_table]
        }

        # Parse the CDP neighbors output to extract interfaces with CDP neighbors
        cdp_interfaces_list = cdp_data['local_interface']
        cdp_interfaces = [string.replace(' ','') for string in cdp_interfaces_list]
        cdp_interfaces = [string.replace('GigabitEthernet','Gi') for string in cdp_interfaces]
        cdp_interfaces = [string.replace('FastEthernet','Fa') for string in cdp_interfaces]
        # Disconnect from the Cisco switch
        net_connect.disconnect()

        # Filter out MAC addresses found on interfaces with CDP neighbors
        filtered_mac_addresses = []
        filtered_ports = []
        filtered_vlans = []
        for mac_address, port, vlan in zip(mac_addresses, ports, vlans):
            if port not in cdp_interfaces and ports.count(port) > 1:
                filtered_mac_addresses.append(mac_address)
                filtered_ports.append(port)
                filtered_vlans.append(vlan)

        # Create a DataFrame to store the filtered MAC addresses, ports, and VLANs
        df = pd.DataFrame({
            'Switch': switch,
            'Port': filtered_ports,
            'MAC Address': filtered_mac_addresses,
            'VLAN': filtered_vlans
        })

        # Save the DataFrame to an Excel file
        with pd.ExcelWriter('mac_table.xlsx', engine='openpyxl', mode='a') as writer:
            df.to_excel(writer, index=False, sheet_name=switch)


print(f"If more than 1 MAC address was found on an interface with no CDP neighbors, it has been saved to mac_table.xlsx")
print('This suggests there is a switch or hub connected to these ports.')