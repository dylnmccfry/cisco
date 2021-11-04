import meraki, json, operator
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
options = []
network_id = ''
c = ""
API_KEY = open('api-key.txt').read()

#root = tk.Tk()
#root.geometry("100x50")

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
        print(' ')
        print(' ')
        print('The network ID for ' + c + ' is ' + network_id)
        print(' ')
        print(' ')
