# reboot_aps.py
## Purpose
This script will connect to a WLC and reboot the APs in the list.

## Usage
1. Fill out the dictionary for the attributes of the WLC.
2. Fill out the list of APs to reboot. The hostname is case sensative for aireOS so be sure to use the exact name of the APs.
```python
python3 reboot_aps.py
Username: admin
Password:
config ap reset AP1

Would you like to reset AP1 ? (y/n)y



(LAB-WLC) >
(LAB-WLC) >
config ap reset AP2

Would you like to reset AP2 ? (y/n)y



(LAB-WLC) >
(LAB-WLC) >

```
