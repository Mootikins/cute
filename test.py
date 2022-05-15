#!/usr/bin/env python3

import argparse
import inspect
from typing import Callable


class CmdGroup:
    def __init__(self):
        self.commands: dict[str, Callable] = {}


def primary_argparse(cmd_groups: dict[str, CmdGroup]):
    help_desc = """
A composable, configurable command toolkit with execution engine.
    """
    parser = argparse.ArgumentParser(description=help_desc)

    subparsers = parser.add_subparsers(
        dest="cmd_group",
        help="Command group to select a command from",
    )
    for (name, group) in cmd_groups.items():
        group_parser = subparsers.add_parser(name)
        cmd_group_subparser = group_parser.add_subparsers(
            dest="cmd",
            help="Command to run",
        )

        for cmd_name, func in group.commands.items():
            cmd_subparser = cmd_group_subparser.add_parser(cmd_name)

            fn_sig = inspect.signature(func)
            for param in fn_sig.parameters.values():
                cmd_subparser.add_argument(
                    "--" + param.name.replace("_", "-"),
                    required=(param.default),
                )

    return parser


def main():
    # TODO: consider adding dynamic conf dir
    # XDG_CONFIG_HOME? hidden dir in home folder?
    from conf import groups

    parser = primary_argparse(groups)
    args = parser.parse_args()

    cmd_group = groups[args.cmd_group]
    cmd = getattr(cmd_group, args.cmd)
    cmd()

    # cmd_group.commands[args.command[0]](args.command_args)


if __name__ == "__main__":
    main()
