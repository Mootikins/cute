import os
import subprocess
import sys

import test


class Directory(test.CmdGroup):
    """
    Commands for editing a directory
    """

    def __init__(self, dir: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
Run ls in a given directory or the default.
        """
        if dir is None:
            dir = self.dir
        try:
            self.chdir()
        except:
            return

        subprocess.run(["ls"])


groups: dict[str, test.CmdGroup] = {
    "home": Directory("~/"),
}
