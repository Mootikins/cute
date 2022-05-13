#!/usr/bin/env python3

from typing import Callable


class CmdGroup:
    def __init__(self):
        self.commands: dict[str, Callable] = {}


def main():
    from conf import environments

    environments["printer"].commands["run"]()


if __name__ == "__main__":
    main()
