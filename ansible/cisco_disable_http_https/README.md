# Disable HTTP and HTTPS on Cisco ios
This script will disable HTTP and HTTPS on Cisco ios devices by first trying to Telnet, if that fails it will then try to SSH.

## Usage
You will need to fill in the hosts file with the hosts that you want this to run against. They are in a group called "[http_devices]". You will then need to fill in the username and password for both SSH and Telnet in the following variables:
ansible_user=<SSH ACCOUNT>
ansible_ssh_pass=<SSH PASSWORD>
ansible_become_password=<ENABLE PASSWORD>

```python
ansible-playbook cisco_disable_http.yml
```
