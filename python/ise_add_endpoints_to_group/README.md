# add_endpoints_to_group.py
## Purpose
This script will connect to ISE and add endpoints located in the txt file, to the specified endpoint group.

## Usage
1. Fill out the macs.txt file with 1 MAC address per line in colon notation.
2. Fill out the variables at the top: ise1 = 'SERVER1.domain.com' ise2 = 'SERVER2.domain.com' endpoint_group_name = 'ENDPOINT GROUP NAME'
```python
python3 add_endpoints_to_group.py USERNAME PASSWORD

python3 add_endpoints_to_group.py admin password12345
Updating existing endpoint: 200
python3 add_endpoints_to_group.py admin password12345
Creating new endpoint and assigning to group: 201
```
