#!/usr/bin/python

# mac_convertor.py - Converts mac address from xx:xx:xx:xx:xx:xx to xxxx-xxxx-xxxx and visa versa.

import re

# Get mac address from user
print("Enter a mac address")
original_mac = input()

# Regexs for mac notation
colon_dash_notation_reg = re.compile('^(([0-9A-Fa-f]{2}[:-]){5})([0-9A-Fa-f]{2})')
hp_notation_reg = re.compile('^([0-9-A-F-a-f]{4}-){2}([0-9A-Fa-f]{4})')

# Check if mac from users is a type of standard notation with dashes or colons, or the notation HP uses.
# for thier switches
if colon_dash_notation_reg.match(original_mac):
    print("Mac is colon dash notation")
    print("Will print out HP notation below and copy to clipboard")
    split_list = re.split(':|-', original_mac)
    hp_mac = split_list[0] + split_list[1] + '-' + split_list[2] + split_list[3] + '-' + split_list[4] + split_list[5]
    print(hp_mac)
elif hp_notation_reg.match(original_mac):
    print("Mac is HP notation")
    print("Will print out standard notation below and copy to clipboard")
    split_list = re.split('-', original_mac)
    first_string = split_list[0]
    second_string = split_list[1]
    thrid_string = split_list[2]
    octet_1 = first_string[0] + first_string[1] + ':'
    octet_2 = first_string[2] + first_string[3] + ':'
    octet_3 = second_string[0] + second_string[1] + ':'
    octet_4 = second_string[2] + second_string[3] + ':'
    octet_5 = thrid_string[0] + thrid_string[1] + ':'
    octet_6 = thrid_string[2] + thrid_string[3]
    print(octet_1 + octet_2 + octet_3 + octet_4 + octet_5 + octet_6)
