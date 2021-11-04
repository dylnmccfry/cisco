import meraki, json, operator, csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
options = []
network_id = ''
c = ""
API_KEY = open('api-key.txt').read()
dashboard = meraki.DashboardAPI(API_KEY)
organization_id = open('org-id.txt').read()

response = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)
for network in response:
    options.append(str(network['name']))
options.sort()

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Locations')

def close_window():
    root.destroy()

def check_cbox(event):
    global c
    c = location_combobox.get() # this will assign the variable c the value of cbox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        global c
        c = ''
        print('User closed selection window. Script cancelled.')
        exit()

label = ttk.Label(text="Select a location:")
label.pack(fill='x', padx=5, pady=5)
selected_location = tk.StringVar()

location_combobox = ttk.Combobox(root, textvariable=selected_location)
location_combobox['values'] = options
location_combobox['state'] = 'readonly'  # normal
location_combobox.pack(fill='x', padx=5, pady=5)
location_combobox.bind('<<ComboboxSelected>>', check_cbox)

root.protocol("WM_DELETE_WINDOW", on_closing)

button = tk.Button(text = "Save", command = close_window)
button.pack()
root.mainloop()

for list_item in response:
    if (list_item["name"] == str(c)):
        network_id = str(list_item["id"])

############################################################
#CLAIMING SECTION###########################################
############################################################

#User enters the network ID for the device to be claimed
device_hostname_list = []
device_serial_list = []
##Gets list for serials and claims them under the chosen Network ID
with open('devices.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
#Read csv file by rows, first value is the serial number, second value is desired hostname
        device_serial = row[0]
        device_hostname = row[1]
#Updates the serial list
        device_serial_list.append(device_serial)
        device_hostname_list.append(device_hostname)
print('Claiming devices...')

response = dashboard.organizations.claimIntoOrganization(
    organization_id,
    serials=device_serial_list
)

response = dashboard.networks.claimNetworkDevices(
    network_id, device_serial_list
)

############################################################
#RENAMING SECTION###########################################
############################################################

print('Renaming devices...')
for device,hostname in zip(device_serial_list,device_hostname_list):
    response = dashboard.devices.updateDevice(
    device,
    name=hostname
    )
    print(response)
