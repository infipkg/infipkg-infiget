#!/bin/bash

echo "setting up directories"

# some operating systems don't have a /usr/local/, so it will create it & child directories if necessary
sudo bash -c "mkdir /usr/local 2> /dev/null"
sudo bash -c "mkdir /usr/local/bin 2> /dev/null"
sudo bash -c "mkdir /usr/local/share 2> /dev/null"

sudo bash -c "mkdir /usr/local/share/termget 2> /dev/null" # create new config directory if one doesn't exist

if [ "$lang" == "1" ]; then
	echo "... installing program to /usr/local/bin"
	chmod +x termget.py
	sudo cp termget.py /usr/local/bin/termget # copy program to PATH
fi

if [ "$lang" == "1" ]; then
	echo -e "\nSuccessfully Installed! If it's not working, try logging out and logging back in again to reset the PATH."
fi
