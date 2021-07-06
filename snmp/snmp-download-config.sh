#!/bin/bash
#Written by Dylan McCaffrey 7/12/2019
echo "######################################################################################"
echo "This script takes the config file from the tftp server and puts it into running-config"
echo "######################################################################################"
echo ""
echo ""
echo "What device should this run on?"
read ip
echo "What is the IP address of the tftp server?"
read tftp
echo "What is the filename the device should copy into running-config?"
read filename
echo "What is the SNMP R/W string?"
read snmp
echo ""
echo ""
echo ""
##Telling that TFTP shall be used
string1="snmpset -c $snmp -v 2c $ip 1.3.6.1.4.1.9.9.96.1.1.1.1.2.336 i 1"

##Source file = running-config
string2="snmpset -c $snmp -v 2c $ip 1.3.6.1.4.1.9.9.96.1.1.1.1.3.336 i 1"

##Destination file = network file
string3="snmpset -c $snmp -v 2c $ip 1.3.6.1.4.1.9.9.96.1.1.1.1.4.336 i 4"

##IP to TFTP-server
string4="snmpset -c $snmp -v 2c $ip 1.3.6.1.4.1.9.9.96.1.1.1.1.5.336 a $tftp"

##filename
string5="snmpset -c $snmp -v 2c $ip 1.3.6.1.4.1.9.9.96.1.1.1.1.6.336 s $filename"

##starts the transfer
string6="snmpset -c $snmp -v 2c $ip 1.3.6.1.4.1.9.9.96.1.1.1.1.14.336 i 1"
echo Starting...
$string1
myvar=$?
if [ $myvar -eq 0 ]; then
	$string2
	myvar=$?

else
	echo Failed to configure tftp setting
	exit 1
fi
if [ $myvar -eq 0 ]; then
	$string3
	myvar=$?

else
	echo Failed to set destination file
	exit 1
fi
if [ $myvar -eq 0 ]; then
	$string4
	myvar=$?
else
	echo Failed to set tftp server
	exit 1
fi
if [ $myvar -eq 0 ]; then
	$string5
	myvar=$?
else
	echo Failed to set filename
	exit 1
fi

if [ $myvar -eq 0 ]; then
	echo Starting the transfer
	$string6
else
	echo Failed to start transfer
	exit 1
fi

exit 0
