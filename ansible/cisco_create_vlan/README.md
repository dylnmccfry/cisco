# Create VLANs
This script will create VLANs, add the SVI's to the Campus Nexus, advertise those network into EIGRP, and configure HSRP settings.

## Usage
You will need to fill in the hosts file with the hosts that you want this to run against. They are in a group called **[ios]** and **[nexus1]** and **[nexus2]** The variables are:
- *ip_helper1* -> DHCP server1
- *ip_helper2* -> DHCP server2
- *vlan_id* -> VLAN ID number
- *vlan_name* -> Name of the VLAN, also used as description for SVI. There is a character limitation on IOS you should limit this to no more than 32 characters.
- *ip_address1* -> Physical IP for the Nexus1 SVI (Usually x.x.x.2)
- *ip_address2* -> Physical IP for the Nexus2 SVI (Usually x.x.x.3)
- *vip_address* -> IP address used for HSRP, Virtual IP (Usually x.x.x.1)
- *hsrp_group* -> HSRP Group number, **must be unique**, number between 0 - 4095 (If using HSRP version 2)
- *interface* -> SVI interface, should match VLAN ID

```python
ansible-playbook cisco_create_vlan.yml -u USERNAME --ask-pass
```
## Notes

You can find which HSRP groups are already in use by executing:

*show hsrp all | i Group*
*Vlan7 - Group 7 (HSRP-V2) (IPv4)*
*Vlan8 - Group 8 (HSRP-V2) (IPv4)*
*Vlan12 - Group 12 (HSRP-V2) (IPv4)*
*Vlan12 - Group 128 (HSRP-V2) (IPv4)*
*Vlan18 - Group 18 (HSRP-V2) (IPv4)*
*Vlan28 - Group 28 (HSRP-V2) (IPv4)*
