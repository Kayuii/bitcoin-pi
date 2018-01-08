# encoding: utf-8
"""Release data for the Bitcoin Pi project."""

#-----------------------------------------------------------------------------
#  Copyright (c) 2018, Evan Qingyan Liu <hmisty@gmail.com>
#
#  Distributed under the terms of the MIT License.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

# Name of the package for release purposes.  This is the name which labels
# the tarballs and RPMs made by distutils, so it's best to lowercase it.
name = 'bitcoin-pi'

# BitcoinPi version information.  An empty _version_extra corresponds to a full
# release.  'dev' as a _version_extra string means this is a development
# version
_version_major = 0
_version_minor = 0
_version_patch = 1
_version_extra = '.dev'
# _version_extra = 'rc2'
#_version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor, _version_patch]

__version__ = '.'.join(map(str, _ver))
if _version_extra:
	__version__ = __version__  + _version_extra

version = __version__  # backwards compatibility name
version_info = (_version_major, _version_minor, _version_patch, _version_extra)

description = "BitcoinPi: Bitcoin cold wallet on raspberry pi zero"

long_description = \
		"""
BitcoinPi provides a bitcoin cold wallet solution on raspberry pi zero.

Its main components are:
	* Online side: running on your computer connected to Internet, for checking balance and creating transactions.
	* Offline side: running on raspberry pi zero, for generating new keys and signing transactions.
	* Cold backup: on paper that locked in your safe cabinet, for life-long saving your assets.

Its feature highlights are:
	* Private keys are never exposed to Internet, and never stored in raw format but always encrypted.
	* Online side can watch only. Offline side will be only needed when signing transactions.
	* Encrypted private keys in pi zero, and backuped on physical paper locked in safe cabinet.
	* Fully open source and thoroughly transparent to you for you to check if any pit-falls. Zero dependency and off-the-shelf on raspberry pi therefore very easy to deploy.
	* Very intuitive interface and fault-proof in design principles.

The latest development version is always available from BitcoinPi's `GitHub
site <https://github.com/hmisty/bitcoin-pi>`_.
"""

license = 'MIT'

authors = {'Evan' : ('Evan Qingyan Liu','hmisty@gmail.com'),
		  }

author = 'Evan Qingyan Liu'

author_email = 'hmisty@gmail.com'

url = 'https://github.com/hmisty/bitcoin-pi'


platforms = ['Linux','Mac OSX','Windows']

keywords = ['Interactive','Shell','Bitcoin','Raspberry','Pi']

classifiers = [
	'Intended Audience :: End Users/Desktop',
	'Intended Audience :: Developers',
	'Intended Audience :: Science/Research',
	'Intended Audience :: Financial and Insurance Industry',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2.7',
	'Topic :: Security :: Cryptography',
	'Topic :: Utilities',
	'Topic :: System :: Shells'
]
