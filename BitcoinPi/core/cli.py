# encoding: utf-8
"""CLI: Command Line Interface."""
#-----------------------------------------------------------------------------
#  Copyright (c) 2018, Evan Qingyan Liu <hmisty@gmail.com>
#
#  Distributed under the terms of the MIT License.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------
from __future__ import print_function

import time
from wallet import *

def print_help():
    """
    Print help messages.
    """

    out = """
    pi help
    pi new
    pi list
    ...
    """
    print(out)

def print_unknown_command(command):
    """
    Unknown command.
    """

    out = """
    Unknown command: %s.""" % command
    print(out)
    print_help()

def create_new_address():
    pass

def list_address():
    wallet_data = load_wallet()
    if wallet_data is not None:
        for i, v in enumerate(wallet_data):
            own = '+' if v.get('ownership') == 'yes' else '-'
            leader = '%s[%s]' % (own, i)
            fmt = '{own}[{i}] {addr} [{alias}]: {memo}'
            out = fmt.format(own=own, i=i, alias=v['alias'], addr=v['address'], memo=v['memo'])
            print(out)

def verify_ownership():
    wallet_data = load_wallet()
    if wallet_data is not None:
        for i, v in enumerate(wallet_data):
            out = 'checking your ownership of {addr} [{alias}]... '.format(addr=v['address'], alias=v['alias'])
            print(out, end='')
            time.sleep(0.5)
            own = 'yes'
            out = own
            print(out)
            v['ownership'] = own

    # save the ownership data back to file
    save_wallet(wallet_data)

def export_key():
    pass

def import_key():
    pass

def sign_message():
    pass

