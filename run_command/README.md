# cisco_run_command.py

This script will prompt you to enter a command you want to run against a list of hosts. By providing a list of IP addresses it will execute that command and send the output to a file named output.txt

## Usage

```python3
python3 cisco_run_command.py
```
## Example Output
```python3
admin@ubuntu:/home/dylan/python-scripts$ python3 show-version.py
Password:
What command would you like to run?
show ver
Enter list of IP addresses. Type "END" to indicate the end of the list, and start the script.
192.168.1.4
192.168.1.4

END
Connecting to devices and running command...Please wait...
Check the output.txt file
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)