# encoding: utf-8
"""Bitcoin Pi: Bitcoin cold wallet on raspberry pi zero."""
#-----------------------------------------------------------------------------
#  Copyright (c) 2018, Evan Qingyan Liu <hmisty@gmail.com>
#
#  Distributed under the terms of the MIT License.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------
from core import cli

def start_pi(argv=None, **kwargs):
    """Launch Bitcoin Pi

    This is a public API method, and will survive implementation changes.

    Parameters
    ----------

    argv : list or None, optional
    If unspecified or None, IPython will parse command-line options from sys.argv.
    To prevent any command-line parsing, pass an empty list: `argv=[]`.

    user_ns : dict, optional
    specify this dictionary to initialize the IPython user namespace with particular values.

    kwargs : various, optional
    Any other kwargs will be passed to the Application constructor,
    such as `config`.
    """

    command = None
    if len(argv) > 1:
        command = argv[1]

    if command is None or command == 'help':
        cli.print_help()
    elif command == 'new':
        cli.create_new_address()
    elif command == 'list':
        cli.list_address()
    elif command == 'ownership':
        cli.verify_ownership()
    elif command == 'export':
        cli.export_key()
    elif command == 'import':
        cli.import_key()
    elif command == 'sign':
        cli.sign_message()
    else:
        # at last
        cli.print_unknown_command(command)

