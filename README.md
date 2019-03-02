# rootOS

Tries to use various CVEs to gain sudo or root access. All exploits have an end goal of adding `ALL ALL=(ALL) NOPASSWD: ALL` to `/etc/sudoers` allowing any user to run `sudo` commands.

![screenshot](screenshot.png)

## Exploits

-   CVE-2015-3760
-   CVE-2015-5889
-   CVE-2017-13872
-   Applescript Dynamic Phishing

## Run

```bash
python root.py
```
