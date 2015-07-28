# Python config changer

a python scrip to modify the configuration of many juniper devices using junos-pyez. 
It requires a file called 'switchlist' which has a list of devices to be modified.
Also requires a file called 'commands' which is the comnands to run on the devices.
The devices need to have netconf enabled and tcp port 830 reachable 
