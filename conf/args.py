import argparse
import inspect
from typing import Callable

from .lib import CmdGroup, CmdGroupMapping


def primary_argparse(cmd_groups: CmdGroupMapping):
    help_desc = """
    A composable, configurable command toolkit with execution engine.
    """
    parser = argparse.ArgumentParser(description=help_desc)

    add_group_subparsers(parser, cmd_groups)

    return parser


def add_group_subparsers(parser, cmd_groups: CmdGroupMapping):
    subparsers = parser.add_subparsers(
        dest="cmd_group",
        title="Command groups",
        required=True,
    )
    for (name, group) in cmd_groups.items():
        add_cmd_subparsers(subparsers, name, group)


def add_cmd_subparsers(parser, name: str, group):
    group_parser = parser.add_parser(name, aliases=group.aliases)
    cmd_group_subparser = group_parser.add_subparsers(
        dest="cmd",
        title="Command to run",
        required=True,
    )

    for cmd_name, cmd_func in group.commands.items():
        add_cmd_to_parser(cmd_group_subparser, cmd_name, cmd_func)


def add_cmd_to_parser(parser, cmd_name: str, cmd_func: Callable):
    cmd_subparser = parser.add_parser(
        cmd_name,
        help=cmd_func.__doc__,
    )

    fn_sig = inspect.signature(cmd_func)
    for param in fn_sig.parameters.values():
        cmd_subparser.add_argument(
            "--" + param.name.replace("_", "-"),
            required=(param.default),
        )
