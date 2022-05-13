import os
import subprocess
import sys
from test import CmdGroup
from typing import Optional


class Printer(CmdGroup):
    def __init__(self, print_string: str = "", dir: Optional[str] = None):
        super().__init__()
        self.print_string = print_string
        self.dir = os.path.expanduser(dir) if dir is not None else dir

        self.commands = {"run": self.run}

    def chdir(self):
        if self.dir is not None:
            try:
                os.chdir(self.dir)
                print(f"{os.getcwd()}")
            except:
                print(f"Could not open dir {self.dir}", file=sys.stderr)
                return

    def run(self):
        try:
            self.chdir()
        except:
            return

        subprocess.run(["ls", "-l"])


environments: dict[str, CmdGroup] = {
    "printer": Printer(print_string="environment 1's string", dir="~/Raven"),
}
