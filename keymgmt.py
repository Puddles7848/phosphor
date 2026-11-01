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

search = input("Select your key. Search with Name, Email, or Comment: ")
print(listKeys(ctx=context, search=search))
