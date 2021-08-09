# Site migration precheks
This requires ansible to be installed please refer to here: [Ansible installation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
## Usage:
Create a folder named ***show-output*** in the same directory as these files.

Fill in the hosts file with the IP addresses of the devices under the group ***precheck_devices***. Then execute the script:

*ansible-playbook cisco_prechecks.yml -u ***USERNAME*** --ask-pass*


Check the folder "show-output" for all of the files.
