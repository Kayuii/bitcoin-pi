# bitcoin-pi

Bitcoin cold wallet solution on raspberry pi zero.

![pizero.png](https://github.com/hmisty/bitcoin-pi/blob/master/pizero.jpg)

Feature highlights:
- Private keys are never exposed to Internet, and never stored in raw format but always encrypted.
- Online side can watch only. Offline side will be only needed when signing transactions.
- Encrypted private keys in pi zero, and backuped on physical paper locked in safe cabinet.
- Fully open source and thoroughly transparent to you for you to check if any pit-falls. Zero dependency and off-the-shelf on raspberry pi therefore very easy to deploy.
- Very intuitive interface and fault-proof in design principles.

## Design ideas

Raspberry pi zero is a neat board (65mm x 30mm x 5mm) that is capable to run a full-fledged Linux system. It is able to bootstrap without any peripherial equipments such as keyboard, monitor, etc, which is called headless bootstrapping. With just a micro-USB to USB cable, it can be run in so-called OTG mode and connected through one-way SSH. Therefore, it would be nice to use pi zero as bitcoin offline wallet together with cold storage as an easy-to-use and safe solution.

The solution is composed of three parts:
- Online side: running on your computer connected to Internet, for checking balance and creating transactions.
- Offline side: running on raspberry pi zero, for generating new keys and signing transactions.
- Cold backup: on paper that locked in your safe cabinet, for life-long saving your assets.

## Use Cases

```
$ pi help
```

### On pi zero (offline side):

#### Create a new address:
```
$ pi new [alias] [memo]
```

Features:
- use hardware entropy for real random seed to generate the key

#### List all addresses:
```
$ pi list
```

#### Most loverable feature! To tell you that you own the addresses and moneys with them.
```
$ pi ownership
```

#### Export a key for printing out or copying to a physical paper to be locked into the safe cabinet, in BIP38 encrypted format.
```
$ pi export [N]
```

#### Import a BIP38 encrypted key, or a raw private key in WIF format but require a passphrase immediately to encrypt it in BIP38 format before saving into the .pi file for safety:
```
$ pi import [key] [alias] [memo]
```

#### Sign the transaction in offline mode:
```
$ pi sign
```

### On computer (online side):

#### List all addresses:
```
$ pi list
```

#### Add an address for use later:
```
$ pi add [address] [alias] [memo]
```

#### Send unspent money from one to another:
```
$ pi send [from alias] [to alias] [amount] [transaction fee]
```
Features:
- direct address send/receive are delibrately unsupported for reducing mistakes
- if amount < unspent of the sender address, it will go back to the sender address by default (i.e. the transaction fee is zero by default)

## The .pi Wallet File

Features:
- human readable
- json format
- private keys are stored in BIP38 encrypted format
- each key has its own passphrase

On pi zero, you have keys:
```
[
	{ "alias": "demo1",
		"address": "1GYUr1QyVdtAEBix4aaPCojv46MYmXCCfg",
		"key": "6PnSXqvvj2VQULV15L2eKqTvYAnbjGcBya5A7sJKtrmcNh2Yh7NVwkkrma",
		"memo": "the first account for demo",
		"ownership": "yes" },
	{ "alias": "1Mtt",
		"address": "1MttLXzk2vTDAUhuvgqhRuMP4HWLWs2ZcR",
		"key": "6PnMHVscBGBspiMLCW4s7M3BRFhpNV5kPxRXas3jMTKTnSEkqZsipDNww2",
		"memo": "the second account for demo",
		"ownership": "yes" },
	{ "alias": "13Y3",
		"address": "13Y3zqRRCCZGiJ6ACsprBgpfKphzyvvTyj",
		"key": "6PnXHXHJMRWLzS1DiVitZqvYcXpB4SD7aCgnzD6EnYJmCXF8SKZK1PbjYB",
		"memo": "the third account for demo",
		"ownership": "yes" }
]
```

On computer, you have no keys (watch-only):
```
[
	{ "alias": "demo1",
		"address": "1GYUr1QyVdtAEBix4aaPCojv46MYmXCCfg",
		"memo": "the first account for demo",
		"ownership": "yes" },
	{ "alias": "1Mtt",
		"address": "1MttLXzk2vTDAUhuvgqhRuMP4HWLWs2ZcR",
		"memo": "the second account for demo",
		"ownership": "yes" },
	{ "alias": "13Y3",
		"address": "13Y3zqRRCCZGiJ6ACsprBgpfKphzyvvTyj",
		"memo": "the third account for demo",
		"ownership": "yes" },
	{ "alias": "hmisty",
		"address": "18mDYwjpirsP1WFBknvpzoArghWyKBXAJQ",
		"memo": "donation address" }
]
```

## Copyright
(c) 2018 Evan Qingyan Liu. hmisty at gmail dot com.

## License
MIT License.
