# encoding: utf-8
"""CLI: Command Line Interface."""
#-----------------------------------------------------------------------------
#  Copyright (c) 2018, Evan Qingyan Liu <hmisty@gmail.com>
#
#  Distributed under the terms of the MIT License.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------
import json
from wallet import *

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

def create_new_address():
    pass

def list_address():
    wallet_data = load_wallet()
    if wallet_data is not None:
        wallet_data = json.loads(wallet_data)
        for i, v in enumerate(wallet_data):
            own = '+' if v.get('ownership') == 'yes' else '-'
            leader = '%s[%s]' % (own, i)
            fmt = '{own}[{i}] {addr} [{alias}]: {memo}'
            print fmt.format(own=own, i=i, alias=v['alias'], addr=v['address'], memo=v['memo'])

def verify_ownership():
    pass

def export_key():
    pass

def import_key():
    pass

def sign_message():
    pass

