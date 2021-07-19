import json
import re
from netmiko import ConnectHandler
import getpass
userPassword = getpass.getpass()
userName = getpass.getuser()
regex = "^[a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9][a-zA-Z][a-zA-Z]$"
statesEast = ["AL", "CT", "DE", "FL", "GA", "IL", "IN", "KY", "ME", "MD", "MA", "MI", "MS", "NH", "NJ", "NY", "NC", "OH", "PA", "RI", "SC", "TN", "VT", "VA", "WV"]
print('Please enter site code:')
siteCode = input()

def checkSite(siteCode):
    if(re.search(regex, siteCode)):
        return(bool(True))

    else:
        return(bool(False))
if checkSite(siteCode) is False:
    print('Invalid site code')
else:
    siteCode = siteCode.upper()

if any(x in siteCode for x in statesEast):
    primaryHostname='US6645NY-CORE-WC01'
    primaryIP='10.10.10.10'
    secondaryHostname='US6645NY-CORE-WC01'
    secondaryIP='10.10.10.10'
else:
    primaryHostname='US6645NY-CORE-WC01'
    primaryIP='10.10.10.10'
    secondaryHostname='US6645NY-CORE-WC01'
    secondaryIP='10.10.10.10'

with open('APs.json') as f:
  apDictionary = json.load(f)

##APs are in this default format APDC8C.37C8.0B80
def checkMac(unformattedMac):
      global Mac
      if len(unformattedMac) == 14 and "." in unformattedMac:
            Mac = unformattedMac.upper()
            Mac = Mac.replace('.', '')
            Mac = Mac[:4] + '.' + Mac[4:]
            Mac = Mac[:9] + '.' + Mac[9:]

#Changes from colon notation

      if len(unformattedMac) == 17 and ":" in unformattedMac:
            Mac = unformattedMac.upper()
            Mac = Mac.replace(':', '')
            Mac = Mac[:4] + '.' + Mac[4:]
            Mac = Mac[:9] + '.' + Mac[9:]

#Changes from hypen notation

      if len(unformattedMac) == 17 and "-" in unformattedMac:
            Mac = unformattedMac.upper()
            Mac = Mac.replace('-', '')
            Mac = Mac[:4] + '.' + Mac[4:]
            Mac = Mac[:9] + '.' + Mac[9:]

      if len(unformattedMac) != 14 and len(unformattedMac) != 17 and unformattedMac != '':
          print('This MAC is not in a supported format:' + ' ' + unformattedMac)
          Mac = 'NULL'

counter = 0
for x in apDictionary:
    checkMac(str(apDictionary[counter]['macAddress']))
    if Mac != 'NULL':
        rename_command = 'config ap name ' + str(apDictionary[counter]['hostname'].upper()) + ' ' + 'AP' + Mac
        ap_mode_command = 'config ap mode flexconnect submode none ' + str(apDictionary[counter]['hostname'].upper())
        ap_flexconnect_group_command = 'config flexconnect group ' + siteCode + ' ' + 'ap add' + ' ' + Mac
        ap_controller_command = 'config ap primary-base' + ' ' + primaryHostname + ' ' + str(apDictionary[counter]['hostname'].upper()) + ' ' + primaryIP
        print(rename_command)
        print(ap_mode_command)
        print(ap_flexconnect_group_command)
        print(ap_controller_command)
        if str(apDictionary[counter]['sdwan'].lower()) == 'yes':
            ap_group_command = 'config ap group-name 128T-Branches' + ' ' + str(apDictionary[counter]['hostname'].upper())
            print(ap_group_command)
        else:
            ap_group_command = 'config ap group-name Branches' + ' ' + str(apDictionary[counter]['hostname'].upper())
            print(ap_group_command)
        counter =+ 1
