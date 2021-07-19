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

###WDC primary, ODC secondary
if any(x in siteCode for x in statesEast):
    print('This is is East of the Mississippi')

##ODC primary, WDC secondary
else:
    print('This site is West of the Mississippi')

print('Enter list of MAC addresses. Type "END" to indicate the end of the list, and start the script.')

macAddr = []
newMAC = input()

def checkMac(unformattedMac):
      if len(unformattedMac) == 14 and "." in unformattedMac:
            Mac = unformattedMac.upper()
            Mac = Mac.replace('.', '')
            Mac = Mac[:2] + ':' + Mac[2:]
            Mac = Mac[:5] + ':' + Mac[5:]
            Mac = Mac[:8] + ':' + Mac[8:]
            Mac = Mac[:11] + ':' + Mac[11:]
            Mac = Mac[:14] + ':' + Mac[14:]
            print(Mac)

#Changes from colon notation

      if len(unformattedMac) == 17 and ":" in unformattedMac:
            Mac = unformattedMac.upper()
            Mac = Mac.replace(':', '')
            Mac = Mac[:2] + ':' + Mac[2:]
            Mac = Mac[:5] + ':' + Mac[5:]
            Mac = Mac[:8] + ':' + Mac[8:]
            Mac = Mac[:11] + ':' + Mac[11:]
            Mac = Mac[:14] + ':' + Mac[14:]
            print(Mac)

#Changes from hypen notation

      if len(unformattedMac) == 17 and "-" in unformattedMac:
            Mac = unformattedMac.upper()
            Mac = Mac.replace('-', '')
            Mac = Mac[:2] + ':' + Mac[2:]
            Mac = Mac[:5] + ':' + Mac[5:]
            Mac = Mac[:8] + ':' + Mac[8:]
            Mac = Mac[:11] + ':' + Mac[11:]
            Mac = Mac[:14] + ':' + Mac[14:]
            print(Mac)

      if len(unformattedMac) != 14 and len(unformattedMac) != 17 and unformattedMac != '':
          print('This MAC is not in a supported format')


while newMAC != 'END':
      newMAC = input()
      if checkMac(newMAC) == True:
         macAddr.append(newMAC)
      if newMAC == 'END' or newMAC == '':
         break
for i in range(len(macAddr)):
    print(macAddr[i]),
