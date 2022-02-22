# Site migration precheks
This requires ansible to be installed please refer to here: [Ansible installation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
## Usage:
Create a folder named ***show-output*** in the same directory as these files.

Fill in the hosts file with the IP addresses of the devices under the group ***precheck_devices***. Then execute the script:

*ansible-playbook cisco_prechecks.yml -u ***USERNAME*** --ask-pass*


Check the folder "show-output" for all of the files.

You can use grep to find a specific MAC/IP for example:

```console
grep -riw "0000.0c9f.abcd" .
   ./file1:10.10.250.1     00:03:44  0000.0c9f.f0fa  Vlan250
grep -riw "10.10.250.1" .
   ./file1:10.10.250.1     00:03:44  0000.0c9f.f0fa  Vlan250
```
