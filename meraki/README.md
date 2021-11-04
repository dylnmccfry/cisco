# Usage
This repo includes a few scripts to speed up deployment of a new Meraki location. This focuses on MR and MS devices.
## Installation
You will need the Meraki Python module installed by using ```python
pip3 install meraki
```
## Usage
Place your api key in the folder these scripts are in. The filename should be api-key.txt Place the org ID in the folder these scripts are in. The filname should be org-id.txt

## get_switch_ports_config.py
This will copy the port configs into json files, in the same folder this script is run from. The filenames will be the serialnumber .json
