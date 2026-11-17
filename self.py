import shlex
import subprocess
import sys
from pathlib import Path

import cmd2


class InteractiveShell(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.intro = "Welcome to Phosphor Interactive Shell"
        self.prompt = "phosphor % "

    def do_contacts(self, argblob: str):
        args = shlex.split(argblob, comments=True, posix=True)
        if args == []:
            subprocess.run(
                [sys.executable, str(Path(__file__).parent / "contacts" / "self.py")],
                check=True,
            )

    # Exiting
    def do_exit(self, arg: str):
        print()
        return True

    do_EOF = do_exit


if __name__ == "__main__":
    InteractiveShell().cmdloop()
