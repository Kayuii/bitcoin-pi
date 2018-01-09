# encoding: utf-8
"""CLI: Command Line Interface."""
#-----------------------------------------------------------------------------
#  Copyright (c) 2018, Evan Qingyan Liu <hmisty@gmail.com>
#
#  Distributed under the terms of the MIT License.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

def print_help():
    """
    Print help messages.
    """

    print """
    pi help
    pi new
    pi list
    ...
    """

def print_unknown_command(command):
    """
    Unknown command.
    """

    print """
    Unknown command: %s.""" % command
    print_help()

