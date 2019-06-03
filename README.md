# rootOS

Tries to use various CVEs to gain sudo or root access. All exploits have an end goal of adding `ALL ALL=(ALL) NOPASSWD: ALL` to `/etc/sudoers` allowing any user to run `sudo` commands.

![screenshot](docs/screenshot.png)

## Exploits

-   CVE-2008-2830
-   CVE-2015-3760
-   CVE-2015-5889
-   CVE-2017-13872
-   CVE-2019-8526
-   AppleScript Dynamic Phishing
-   [Sudo Piggyback](https://www.n00py.io/2016/10/privilege-escalation-on-os-x-without-exploits/)

## Run

```bash
python root.py
```

## Dynamic Phishing

![phishing](docs/phishing.png)

![phishing_id](docs/phishing_id.png)
