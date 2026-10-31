import json
import os
import pathlib
from types import SimpleNamespace
from typing import Any

import platformdirs

# Define app (platformdirs)
APPNAME = "phosphor"
AUTHOR = "Puddles7848"

# Paths
paths = SimpleNamespace()
## Data
paths.data = platformdirs.user_data_path(
    appname=APPNAME, appauthor=AUTHOR, ensure_exists=True
)
## Config
paths.config = platformdirs.user_config_path(
    appname=APPNAME, appauthor=AUTHOR, ensure_exists=True
)


# High level file operations
## Read
def loadJson(fp: os.PathLike[str]) -> Any:
    fp = pathlib.Path(fp)
    with fp.open("rt", encoding="utf8") as fd:
        json.load(fd)


## Write (Atomic)
def write(fp: os.PathLike[str], content: Any) -> None:
    fp = pathlib.Path(fp)
    tempFp = fp.with_suffix(fp.suffix + "swp")

    # Write temp file
    with tempFp.open("wt", encoding="utf8") as fd:
        json.dump(content, fd, indent=4)

        fd.flush()
        os.fsync(fd.fileno())

    # Replace file
    tempFp.replace(fp)

    # Open and sync parent dir
    parentFd = os.open(fp.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(parentFd)
    finally:
        os.close(parentFd)

## Exists?
def exists(fp: os.PathLike[str]) -> bool:
    return pathlib.Path(fp).exists()
