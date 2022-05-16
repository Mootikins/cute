#!/usr/bin/env python3

import argparse
import inspect
from typing import Callable


class CmdGroup:
    def __init__(self, aliases=[]):
        self.commands: dict[str, Callable] = {}
        self.aliases = aliases


def primary_argparse(cmd_groups: dict[str, CmdGroup]):
    help_desc = """
A composable, configurable command toolkit with execution engine.
    """
    parser = argparse.ArgumentParser(description=help_desc)

    subparsers = parser.add_subparsers(
        dest="cmd_group",
        title="Command groups",
        required=True,
    )
    for (name, group) in cmd_groups.items():
        group_parser = subparsers.add_parser(name, aliases=group.aliases)
        cmd_group_subparser = group_parser.add_subparsers(
            dest="cmd",
            title="Command to run",
            required=True,
        )

        for cmd_name, cmd_func in group.commands.items():
            cmd_subparser = cmd_group_subparser.add_parser(
                cmd_name,
                help=cmd_func.__doc__,
            )

            fn_sig = inspect.signature(cmd_func)
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
