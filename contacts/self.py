import cmd
import shlex


class InteractiveShell(cmd.Cmd):
    prompt = "contacts % "

    # Exiting
    def do_exit(self, arg: str):
        print()
        return True

    do_EOF = do_exit


if __name__ == "__main__":
    InteractiveShell().cmdloop()
