## Fill out the routes.txt file with just CIDR notation routes from your network.
The easiest way using Cisco is to use "sh ip route | i ubest" on NX-OS for example. And then in a text editor remove everything after the comma. Nothing will be printed if the subnets do not overlap.

```python
python3 check-overlapping-subnets.py
Enter a CIDR subnet to check: 10.1.0.128/25
10.1.0.128/25 Overlaps with 10.1.0.0/24

python3 check-overlapping-subnets.py
Enter a CIDR subnet to check: 10.1.2.0/26


```
