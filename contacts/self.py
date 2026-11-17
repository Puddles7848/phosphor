import shlex

import cmd2


class InteractiveShell(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "contacts % "

    # Exiting
    def do_exit(self, arg: str):
        print()
        return True

    do_EOF = do_exit


if __name__ == "__main__":
    InteractiveShell().cmdloop()
