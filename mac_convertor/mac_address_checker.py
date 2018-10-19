#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# mac_address_address_checker.py - Takes list of mac_address addresses for input.
# Checks to see what notation they are in a prints out the oppiste notation


def check_mac_address(mac_address):
    # Regexs for mac_address notation
    colon_dash_notation_reg = re.compile(
        '^(([0-9A-Fa-f]{2}[:-]){5})([0-9A-Fa-f]{2})')
    hp_notation_reg = re.compile('^([0-9-A-F-a-f]{4}-){2}([0-9A-Fa-f]{4})')
    no_colon_notation_reg = re.compile('^([0-9-A-F-a-f]{12})')

    # Check what notation is used for the mac_address address
    # If standard notation is used switch to HP notation
    if colon_dash_notation_reg.match(mac_address):
        split_list = re.split(':|-', mac_address)
        hp_mac_address = split_list[0] + split_list[1] + '-' + split_list[2] + \
            split_list[3] + '-' + split_list[4] + split_list[5]

        return hp_mac_address

    # If HP notation is used switch to standard notation 
    elif hp_notation_reg.match(mac_address):
        split_list = re.split('-', mac_address)
        first_string = split_list[0]
        second_string = split_list[1]
        thrid_string = split_list[2]
        octet_1 = first_string[0] + first_string[1] + ':'
        octet_2 = first_string[2] + first_string[3] + ':'
        octet_3 = second_string[0] + second_string[1] + ':'
        octet_4 = second_string[2] + second_string[3] + ':'
        octet_5 = thrid_string[0] + thrid_string[1] + ':'
        octet_6 = thrid_string[2] + thrid_string[3]

        return octet_1 + octet_2 + octet_3 + octet_4 + octet_5 + octet_6

    # If the mac_address is displayed as a string of 12 characters then switch to standard notation. 
    elif no_colon_notation_reg.match(mac_address):
        n = 2
        new = [mac_address[i:i+n] for i in range(0, len(mac_address), n)]
        return new[0] + ":" + new[1] + ":" + new[2] + ":" + new[3] + ":" + new[4] + ":" + new[5]

    else:
        return None
