import sys
from pathlib import Path

import gnupg

import fs

fs.loadJson(Path(fs.paths.config / "keyMgmt.json"), fallback={})

try:
    gpg = gnupg.GPG()
except ValueError:
    print("""
GNUPG is not installed!
    Windows download: https://www.gpg4win.org/download.html
    Mac installer: https://formulae.brew.sh/formula/gnupg#default
        *You will need to install the brew package manager.
    GNU + Linux:
        sudo pacman -S gnupg # Arch and friends
        sudo apt install gnupg # Debian and friends (Ubuntu, Mint)
        sudo dnf install gnupg2 # Fedora
    Android (Termux):
        pkg install gnupg
    BSD:
        sudo pkg install gnupg # FreeBSD
        doas pkg_add gnupg # OpenBSD
        sudo pkgin install gnupg # FreeBSD
            *pkgin on FreeBSD is not always installed, mostly a convience
            package manager
In very rare cases, you might not have a home directory! If you managed to not
have one, it is expected you know how to... create it back (╥﹏╥)
""")
    sys.exit(1)

# GNUPG Home
print(gpg.gnupghome)
