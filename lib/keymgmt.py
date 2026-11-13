from pathlib import Path

import fs
import gpgme

config = fs.loadJson(Path(fs.paths.config / "keyMgmt.json"), fallback={})

ctx = gpgme.Context()


def listKeys(ctx: gpgme.Context, search: str | None = None) -> list[gpgme.Key]:
    if search is None:
        return list(ctx.keylist())
    else:
        return list(ctx.keylist(search))


def getFingerprint(key: gpgme.Key, number: int):
    return key.subkeys[number].fpr


def getName(key: gpgme.Key, number: int):
    return key.uids[number].name


def getEmail(key: gpgme.Key, number: int):
    return key.uids[number].email


def displayKey(key: gpgme.Key):  # DEFAULTS TO PRIMARY
    return f"{getFingerprint(key, 0)} | {getName(key, 0)} | {getEmail(key, 0)}"
