# cisco_prechecks.py

This script will run the following commands against a list of hosts:
```bash
show int status
show run
show cdp nei
show ip arp
```
By providing a list of IP addresses it will execute those commands and send the output to a text file for each host, the filename is the IP address.

## Usage

```python3
python3 cisco_prechecks.py
```
## Example Output
```python3
admin@ubuntu:/home/dylan/python-scripts$ python3 cisco_prechecks.py
Username:
Password:
Alternate local account in case TACACS+ isn't working:
Password:
Enter list of IP addresses. Type "END" to indicate the end of the list, and start the script.
192.168.1.4
192.168.1.5
192.168.1.6
END
Connecting to devices and running command...Please wait...
Connecting to 192.168.1.4
Connecting to 192.168.1.5
Connecting to 192.168.1.6
Check the output files.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)
