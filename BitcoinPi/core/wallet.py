# encoding: utf-8
"""Operations on .pi Wallet File."""
#-----------------------------------------------------------------------------
#  Copyright (c) 2018, Evan Qingyan Liu <hmisty@gmail.com>
#
#  Distributed under the terms of the MIT License.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------
import os
import shutil
from constant import *

wallet_filepath = None
def get_wallet_filepath():
    """
    Returns the wallet filepath currently used.
    """
    return wallet_filepath

def load_wallet():
    """
    Seek and load .pi wallet file named .bitcoin.pi .
    Firstly, seek working dir.
    If not found, seek home dir.
    If not found still, raise error.
    """
    wallet_data = None
    for loc in wallet_file_loc:
        filepath = os.path.join(loc, wallet_file_name)
        if os.path.exists(filepath):
            wallet_filepath = filepath
            print 'Using', filepath, '.'
            with open(filepath, 'r') as f:
                wallet_data = f.read()

    if wallet_data == None:
        print 'No wallet found. Execute "pi new" to create one?'

    return wallet_data

def save_wallet(wallet_data):
    """
    Save wallet data to disk file with wallet_filepath.
    Returns filepath of the saved wallet.
    """
    filepath = get_wallet_filepath()
    if os.path.exists(filepath):
        print 'Backup existing wallet file', filepath, 'to', wallet_file_backup, '.'
        shutil.copyfile(filepath, wallet_file_backup)
        with open(filepath, 'w') as f:
            f.write(wallet_data)
    else:
        print 'Create a new wallet file', filepath
        with open(filepath, 'w') as f:
            f.write(wallet_data)

    print 'Wallet', filepath, 'successfully saved.'
    return filepath

