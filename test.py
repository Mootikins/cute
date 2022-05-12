#!/usr/bin/env python3

from abc import ABC
import sys
from typing import Callable


class Env(ABC):
    commands: dict[str, Callable]


def main():
    sys.path.insert(1, "/Users/moot/")

    from conf import environments

    environments["printer"].commands["run"]()


if __name__ == "__main__":
    main()
