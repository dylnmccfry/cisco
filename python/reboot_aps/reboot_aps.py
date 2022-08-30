from netmiko import ConnectHandler
import getpass

un = input("Username: ")
pw = getpass.getpass()

cisco_wlc = {
    'device_type': 'cisco_wlc_ssh',
    'host': '10.10.10.10',
    'username': un,
    'password': pw,
    'port': 22,
}

wlc_connect = ConnectHandler(**cisco_wlc)
aps = ['AP1', 'AP2', 'AP3', 'AP4']
for ap_name in aps:
    cmd_list = [
    [f"config ap reset {ap_name}", r"Would you like"],
    ["y", ""]
    ]
    output = wlc_connect.send_multiline(cmd_list)
    print(output)

wlc_connect.disconnect()
