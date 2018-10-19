#!/usr/bin/python

# mac_convertor.py - Converts mac address from
# xx:xx:xx:xx:xx:xx to xxxx-xxxx-xxxx and visa versa.

import argparse
import mac_address_checker


def main():
    # Handle command line args
    parser = argparse.ArgumentParser(description='Process some mac addresses.')
    parser.add_argument('-m', '--mac-addresses', nargs='+',
                        help='Enter one or more mac addresses' +
                        'seperated by a space')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'),
                        help='File with one mac address per line')
    args = parser.parse_args()

    # Check if mac addresses were entered on the cli or a file was passed
    if args.mac_addresses:
        mac = mac_address_checker.check_mac_address(args.mac_addresses)
        print(mac)
    elif args.file:
        macs = args.file.readlines()
        macs = [x.strip() for x in macs]
        for mac in macs:
            print(mac_address_checker.check_mac_address(mac))

if __name__ == '__main__':
    main()
