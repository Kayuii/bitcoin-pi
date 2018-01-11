# encoding:utf-8
"""
Pre-definitions of constants.
"""
#-----------------------------------------------------------------------------
#  Copyright (c) 2018, Evan Qingyan Liu <hmisty@gmail.com>
#
#  Distributed under the terms of the MIT License.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------
import os
from os.path import expanduser

wallet_file_loc = [os.getcwd(), expanduser('~')] # current dir first, hoem dir second
wallet_file_name = '.bitcoin.pi'
wallet_file_backup_suffix = '.bak'

