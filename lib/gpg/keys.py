import gpgme

ctx = gpgme.Context()

key = next(iter(ctx.keylist("puddles7848@gmail.com")))  # TEST


# List of keys
def parse_keylist() -> list[gpgme.Key]:
    return list(ctx.keylist())


# What can this key/subkey do?
def parse_key_abilities(key: gpgme.Key | gpgme.Subkey) -> dict[str, bool]:
    return {
        "authenticate": key.can_authenticate,
        "certify": key.can_certify,
        "encrypt": key.can_encrypt,
        "sign": key.can_sign,
    }


# Do we have both sides of the key/subkey?
def parse_key_secret_available(key: gpgme.Key | gpgme.Subkey) -> bool:
    return key.secret


# Can this key/subkey be used?
def parse_key_validity(key: gpgme.Key | gpgme.Subkey) -> bool:
    return not key.disabled and not key.expired and not key.revoked


# What uids are in this key?
def parse_key_indentities(key: gpgme.Key) -> dict[str, str]:
    uids = list(key.uids)
    uids_dict = {}

    for i in range(len(uids)):
        cuid = uids[i]  # current uid
        uids_dict[i] = {
            "name": cuid.name,
            "email": cuid.email,
            "comment": cuid.comment,
            "display": cuid.uid,
        }

    return uids_dict


# What subkeys are in this key?
def parse_key_subkeys(key: gpgme.Key) -> dict[str, str]:
    subkeys = list(key.subkeys)
    subkeys_dict = {}

    for i in range(len(subkeys)):
        csubkey = subkeys[i]  # current subkey
        subkeys_dict[i] = {
            "abilities": parse_key_abilities(csubkey),
            "fingerprint": csubkey.fpr,
            "secret_available": parse_key_secret_available(csubkey),
            "usable": parse_key_validity(csubkey),
        }

    return subkeys_dict


# What's the key's trust?
def parse_key_trust(key: gpgme.Key) -> int:
    return key.owner_trust


# Do it
def parse_key_full(key: gpgme.Key):
    return {
        "abilities": parse_key_abilities(key),
        "uids": parse_key_indentities(key),
        "secret_available": parse_key_secret_available(key),
        "subkeys": parse_key_subkeys(key),
        "trust": parse_key_trust(key),
        "validity": parse_key_validity(key),
    }


# TEST
print(parse_key_full(key))
