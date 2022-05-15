import os
import subprocess
import sys
from test import CmdGroup


class Directory(CmdGroup):
    """
    Commands for editing a directory
    """
    def __init__(self, dir: str):
        super().__init__()
        self.dir = os.path.expanduser(dir)

        self.commands = {"ls": self.ls, "chdir": self.chdir}

    def chdir(self, dir=None):
        if dir is None:
            dir = self.dir
        try:
            os.chdir(self.dir)
        except:
            print(f"Could not open dir {self.dir}", file=sys.stderr)
            return

    def ls(self, dir=None):
        """
        Help text for ls.
        """
        if dir is None:
            dir = self.dir
        try:
            self.chdir()
        except:
            return

        subprocess.run(["ls"])


groups: dict[str, CmdGroup] = {
    "home": Directory("~/"),
}
