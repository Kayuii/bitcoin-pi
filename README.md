# bitcoin-pi

![pizero.png](https://github.com/hmisty/bitcoin-pi/blob/master/pizero.jpg)

# Design ideas

Raspberry pi zero is a neat board (65mm x 30mm x 5mm) that is capable to run a full-fledged Linux system. It is able to be bootstrapped without any peripherial equipments such as keyboard, monitor, etc, which is called headless bootstrapping. With just a micro-USB to USB cable, it can be run in so-called OTG mode and connected through one-way SSH. Therefore, it would be nice to use pi zero as bitcoin offline wallet together with cold storage as an easy-to-use and safe solution.

The solution is composed of three parts:
	- online side: running on your computer connected to Internet, for checking balance and creating transactions.
	- offline side: running on raspberry pi zero, for generating new keys and signing transactions.
	- cold backup: on paper that locked in your safe cabinet, for life-long saving your assets.

# Use Cases

On pi zero:

$ pi help

$ pi new

$ pi list

$ pi export 0

$ pi import

$ pi sign

On computer:

$ pi send


