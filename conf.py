import os
import sys
from subprocess import call
from test import Env
from typing import Optional


class Printer(Env):
    def __init__(self, print_string: str = "", dir: Optional[str] = None):
        self.print_string = print_string
        self.dir = os.path.expanduser("~/Desktop") if dir is not None else dir

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

        call("ls -l")


environments: dict[str, Env] = {
    "printer": Printer(print_string="environment 1's string", dir="~/Desktop"),
}
