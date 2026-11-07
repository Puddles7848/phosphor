import sys
from pathlib import Path

import gpgme

import fs

config = fs.loadJson(Path(fs.paths.config / "keyMgmt.json"), fallback={})

context = gpgme.Context()
context.keylist()

def listKeys(ctx: gpgme.Context, search: str|None=None) -> list[gpgme.Key]:
    if search is None:
        return list(ctx.keylist())
    else:
        return list(ctx.keylist(search))

def getFingerprint(key: gpgme.Key):
    fingerprints = []

    for i in range(len(key.subkeys)):
        fingerprints.append(key.subkeys[i].fpr)

    return fingerprints

if not config.get("gpg.selectedKey", ""):
    searchQuery = input("Search keys | ")
    searchResult = listKeys(context, searchQuery)
