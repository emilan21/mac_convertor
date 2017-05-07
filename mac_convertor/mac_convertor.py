#!/usr/bin/python

# mac_convertor.py - Converts mac address from xx:xx:xx:xx:xx:xx to xxxx-xxxx-xxxx and visa versa.

import re

print("Enter a mac address")
original_mac = input()

colon_dash_notation_reg = re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})')
hp_notation_reg = re.compile('^([0-9-A-F-a-f]{4}-){2}([0-9A-Fa-f]{4})')

if original_mac == colon_dash_notation_reg.search(original_mac):
    reg_obj = colon_dash_notation_reg.search(original_mac)
    hp_mac = 
