###Imports regex module
import re
###Imports netmiko module
from netmiko import ConnectHandler
###Imports getpass module for username and password functions
import getpass
#userName = getpass.getuser()
userName = input("Username: ")
userPassword = getpass.getpass()
###Sets counter used in loop to reference device in ipAddr list
counter = 0
###Sets regex to check if IP address is valid
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
###Assigns variable for the command the user is trying to run
print('What command would you like to run?')
command = input()
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
print('Connecting to devices and running command...Please wait...')
for ip in ipAddr:
    print("Connecting to " + ip)
    try:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ipAddr[counter], username=userName, password=userPassword)
        output = net_connect.send_command(command)
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        net_connect.disconnect()
#Fallback section in case first username doesn't work
    except:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ipAddr[counter], username="username", password="password")
        output = net_connect.send_command(command)
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        net_connect.disconnect()
#Fallback to trying Telnet if SSH section above doesn't work
    except:
        net_connect = ConnectHandler(device_type='cisco_ios_telnet', host=ipAddr[counter], username=userName, password=userPassword)
        output = net_connect.send_command(command)
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        net_connect.disconnect()
    except:
        net_connect = ConnectHandler(device_type='cisco_ios_telnet', host=ipAddr[counter], username="username", password="password")
        output = net_connect.send_command(command)
        print(output, file=open(ipAddr[counter] + '.txt', "a"))
        net_connect.disconnect()
    counter += 1
print('Check the output files created.')
