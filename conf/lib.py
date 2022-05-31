from typing import Callable


class CmdGroup:
    def __init__(self, aliases=[]):
        self.commands: dict[str, Callable] = {}
        self.aliases = aliases

CmdGroupMapping = dict[str, CmdGroup]
