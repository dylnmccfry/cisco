# Disable HTTP and HTTPS on Cisco ios
This script will disable vstack on Cisco ios devices.

## Usage
You will need to fill in the hosts file with the hosts that you want this to run against. They are in a group called "[vstack_devices]". You will then need to fill in the username and password for the following variables:
#### ansible_user=```USERNAME```
#### ansible_ssh_pass=```PASSWORD```
#### ansible_become_password=```ENABLE PASSWORD```

```python
ansible-playbook cisco_disable_vstack.yml -u USERNAME --ask-pass
```
