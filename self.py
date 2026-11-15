import cmd
import shlex
import subprocess
import sys
from pathlib import Path


class InteractiveShell(cmd.Cmd):
    intro = "Welcome to Phosphor Interactive Shell"
    prompt = "phosphor % "

    def do_contacts(self, argblob: str):
        args = shlex.split(argblob, comments=True, posix=True)
        if args == []:
            subprocess.run(
                [sys.executable, str(Path(__file__).parent / "contacts" / "self.py")],
                check=True
            )

    # Exiting
    def do_exit(self, arg: str):
        print()
        return True

    do_EOF = do_exit


if __name__ == "__main__":
    InteractiveShell().cmdloop()
