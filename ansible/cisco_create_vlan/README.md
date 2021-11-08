# Create VLANs
This script will create VLANs, add the SVI's to the Campus Nexus, advertise those network into EIGRP, and configure HSRP settings.

## Usage
You will need to fill in the hosts file with the hosts that you want this to run against. They are in a group called **[ios]** and **[nexus1]** and **[nexus2]** The variables are:
- *ip_helper1* -> DHCP server1
- *ip_helper2* -> DHCP server2
- *vlan_id* -> VLAN ID number
- *vlan_name* -> Name of the VLAN, also used as description for SVI
- *ip_address1* -> Physical IP for the Nexus1 SVI
- *ip_address2* -> Physical IP for the Nexus2 SVI
- *vip_address* -> IP address used for HSRP, Virtual IP
- *hsrp_group* -> HSRP Group number, must be unique, number between 0 - 4095
- *interface* -> SVI interface, should match VLAN ID

```python
ansible-playbook cisco_create_vlan.yml -u USERNAME --ask-pass
```
