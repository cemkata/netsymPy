# netsymPy
python based web interface for netem, tc

The program uses Bottle: Python Web Framework. (https://bottlepy.org/docs/dev/#)

This doesn`t work on windows. 

the program alows to add delete and change rules for the tc.
tc is a programm that alows to simulate diffrent network behaivour.

To run it you need python3 and iproute or iproute2 package installed on the linux.

To install it you can either download the pyNetsimInstaler.sh 
Change the permitions to be executable.
And start:
 - createDB.sh
 - editConfig.sh
And start it with root permitions. 

You will be asked if you want to start automatically or just to unpack it.

In order to the pyNetsim to work corectly you have to start it with root permitions.

All scripts have to start with root permitions.

If you dont want to use the instalation script
after downloading you should replace "pythonScripts/bottle.py" with the file from https://github.com/bottlepy/bottle/raw/master/bottle.py

*Note: If the nic interface is wrong you can replace the printif.sh with one of printif1.sh	or printif2.sh or printif3.sh or printif4.sh.
       In case none of the scripts work create one manualy just echoing each interface name one at a time like printif5.sh

TODO
make better logging.
For now eitehr it logs almost everzthing or nothing.
