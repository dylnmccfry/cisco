###Imports regex module
import re
###Imports netmiko module
from netmiko import ConnectHandler
###Imports getpass module for username and password functions
import getpass
#userName = getpass.getuser()
userName = input("Username: ")
userPassword = getpass.getpass()
altUser = input("Alternate local user account in case TACACS+ isn't working: ")
altPassword = getpass.getpass()
###Sets counter used in loop to reference device in ipAddr list
counter = 0
###Sets regex to check if IP address is valid
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
###Asks user to enter IP and assigns it to newIP variable, creates ipAddr list
print('Enter list of IP addresses. Type "END" to indicate the end of the list, and start the script.')
ipAddr = []
newIP = input()
###Creates function to check if IP address is valid
def check(newIP):
    if(re.search(regex, newIP)):
        return(bool(True))

    else:
        return(bool(False))

###If IP address is valid, appends to ipAddr list
if check(newIP) == True:
    ipAddr.append(newIP)
while newIP != 'END':
      newIP = input()
      if check(newIP) == True:
         ipAddr.append(newIP)
      if newIP == 'END':
         break
print('Connecting to devices and running prechecks...Please wait...')
for ip in ipAddr:
    print("Connecting to " + ip)
    try:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ipAddr[counter], username=userName, password=userPassword)
        output = net_connect.send_command('show cdp neighbor')
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        output = net_connect.send_command('show run')
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        output = net_connect.send_command('show int status')
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        output = net_connect.send_command('show ip arp')
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        output = net_connect.send_command('show mac address-table')
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        net_connect.disconnect()
#Fallback section in case first username doesn't work
    except:
        try:
            net_connect = ConnectHandler(device_type='cisco_ios', host=ipAddr[counter], username=altUser, password=altPassword)
            output = net_connect.send_command('show cdp neighbor')
            print(output, file=open(ipAddr[counter] + '.txt', "a"))
            output = net_connect.send_command('show run')
            print(output, file=open(ipAddr[counter] + '.txt', "a"))
            output = net_connect.send_command('show int status')
            print(output, file=open(ipAddr[counter] + '.txt', "a"))
            output = net_connect.send_command('show ip arp')
            print(output, file=open(ipAddr[counter] + '.txt', "a"))
            output = net_connect.send_command('show mac address-table')
            print(output, file=open(ipAddr[counter] + '.txt', "a"))
            net_connect.disconnect()
    #Fallback to trying Telnet if SSH section above doesn't work
        except:
            try:
                net_connect = ConnectHandler(device_type='cisco_ios_telnet', host=ipAddr[counter], username=userName, password=userPassword)
                output = net_connect.send_command('show cdp neighbor')
                print(output, file=open(ipAddr[counter] + '.txt', "a"))
                output = net_connect.send_command('show run')
                print(output, file=open(ipAddr[counter] + '.txt', "a"))
                output = net_connect.send_command('show int status')
                print(output, file=open(ipAddr[counter] + '.txt', "a"))
                output = net_connect.send_command('show ip arp')
                print(output, file=open(ipAddr[counter] + '.txt', "a"))
                output = net_connect.send_command('show mac address-table')
                print(output, file=open(ipAddr[counter] + '.txt', "a"))
                net_connect.disconnect()
            except:
                try:
                    net_connect = ConnectHandler(device_type='cisco_ios_telnet', host=ipAddr[counter], username=altUser, password=altPassword)
                    output = net_connect.send_command('show cdp neighbor')
                    print(output, file=open(ipAddr[counter] + '.txt', "a"))
                    output = net_connect.send_command('show run')
                    print(output, file=open(ipAddr[counter] + '.txt', "a"))
                    output = net_connect.send_command('show int status')
                    print(output, file=open(ipAddr[counter] + '.txt', "a"))
                    output = net_connect.send_command('show ip arp')
                    print(output, file=open(ipAddr[counter] + '.txt', "a"))
                    output = net_connect.send_command('show mac address-table')
                    print(output, file=open(ipAddr[counter] + '.txt', "a"))
                    net_connect.disconnect()
                except:
                    print("Unable to connect to device using SSH or Telnet")

    counter += 1
print('Done.')
