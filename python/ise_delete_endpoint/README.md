# delete_endpoint.py
## Purpose
This script will connect to ISE and delete endpoints located in the txt file.

## Usage
1. Fill out the macs.txt file with 1 MAC address per line in colon notation.
2. Fill out the variable at the top: ise1 = 'SERVER1.domain.com'
```python
python3 delete_endpoint.py
  Username: admin
  Password: PASS
  Deleteing endpoint 204
  Deleteing endpoint 204
  Deleteing endpoint 204
  Deleteing endpoint 204
python3 delete_endpoint.py
  Username: admin
  Password: PASS
  aa:aa:bb:bb:0b:60 was not found
  aa:aa:bb:bb:0b:61 was not found
  aa:aa:bb:bb:0b:62 was not found
  aa:aa:bb:bb:0b:63 was not found

```
