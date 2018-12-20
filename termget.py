#!/usr/bin/env python3
import os
import time
import sys
import getpass

# Colors (Thanks to Linux /usr/ for this code)
bold = "\033[1m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
print(reset) # disable all color on start

package = " "

# The TermGet SPLASHSCREEN
termgetBig = """
_________  _______   _______   _______   _______   _______  _________
\__   __/ (  ____ \ (  ____ ) (       ) (  ____ \ (  ____ \ \__   __/
   ) (    | (    \/ | (    )| | () () | | (    \/ | (    \/    ) (
   | |    | (__     | (____)| | || || | | |       | (__        | |
   | |    |  __)    |     __) | |(_)| | | | ____  |  __)       | |
   | |    | (       | (\ (    | |   | | | | \_  ) | (          | |
   | |    | (____/\ | ) \ \__ | )   ( | | (___) | | (____/\    | |
   )_(    (_______/ |/   \__/ |/     \| (_______) (_______/    )_(
"""

def multichoicePrompt(string):
    breakdoublereturn = string.split("\n\n") # top part is white bold, so split by double return will separate
    returnstr = reset + bold + breakdoublereturn[0] + "\n\n" # put top part in return
    mag = True # magenta? boolean

    for line in breakdoublereturn[1].split("\n"): # interlace the colors for each line
        if mag == True:
            returnstr = returnstr + bold + magenta + line + reset + "\n"
            mag = False
        else:
            returnstr = returnstr + bold + blue + line + reset + "\n"
            mag = True
    return returnstr + "\n" # final return (with extra newline) for function

try:
    version = "2.2" # version number

    credit = magenta + (
        "TermGet was created by:\n"
        "- PizzaLovingNerd (main developer)\n"
        "- SadError256\n"
        "- Linux /usr/"
        "- Emil Engler"
        )
	
    def askreturn(): input(reset + yellow + "\nPress enter to continue")

    # Imports libraries and sets variables

    def pickManager():
        return multichoicePrompt(
            "\nPlease choose a package manager:\n"
            "\n1. apt-get (For Debian, and Debian based systems.)"
            "\n2. xbps (For Void Linux, and Void Linux based systems)"
            "\n3. dnf (For Fedora, and Fedora based systems)"
            "\n4. yum (For older versions of Fedora, and older Fedora based systems)"
            "\n5. zypper (For OpenSUSE, and OpenSUSE based systems)"
            "\n6. eopkg (For Solus, and Solus based systems)"
            "\n7. pacman (For Arch, and Arch based systems)"
            "\n8. emerge(For Gentoo, and Gentoo based systems)"
            "\n9. pkg (for FreeBSD, and FreeBSD based systems.)"
            "\n10. chromebrew (for Chrome OS, Chromium OS, CloudReady, and ZayuOS)"
            "\n11. homebrew (for macOS/Mac OS X)"
            "\n12. nix (For NixOS, and NixOS based systems.)"
        )

    if len(sys.argv) == 2:
        elif sys.argv[1] == "pip3": package = "pip3"
        elif sys.argv[1] == "pip2": package = "pip2"
        elif sys.argv[1] == "pip": package = "pip"
        elif sys.argv[1] == "apm": package = "apm"
        elif sys.argv[1] == "nix": package = "nix"
	else: package =	"infipkg"
            
	print(reset + yellow + "package manager set to " + package)
    # Checks for command line argument

    def clear(): os.system("clear")
    # Runs "clear" over shell to clear the screen.

    clear()
    print(reset + bold + termgetBig + "\n\nThis is version " + version)

    # MEOW!

    if package = "infipkg":
        while True:  # Starts a loop
            clear()

            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Remove an application"
                "\n4. Update all packages"
                "\n5. Update Database"
                "\n6. Clean"
                "\n7. Credits"
                "\n8. Exit"
                "\n9. Enter shell\n\n"))  # Asks for user input

            if user == "1":  # Search
				clear()
                # Insert code
				askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print(reset + "")
                os.system("sudo infipkg install " + user)

            if user == "3":  # Remove MEOW
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print(reset + "")
                os.system("sudo infipkg remove " + user)
                askreturn()

            if user == "4":  # Updates Packages
				clear()
				# Insert Code Here
                askreturn()

            if user == "5":  # Updates Database MEOW
                clear()
                # Insert Code
                askreturn()

            if user == "6":  # Cleans
				clear()
				# Insert Code
				askreturn()

            if user == "7":  # Credits

                clear()
                print(credit)
                time.sleep(3)

            if user == "8":
                print(reset)
                clear()
                quit()

            if user == "9":
                clear()
                print(reset + "Entering bash...")
                print(reset + "Press CTRL+D or type \"exit\" to return to TermGet.")
                os.system("bash")
                print(reset + "Returning to termget...")
                clear()

    if package == "pip" or package == "pip2" or package == "pip3":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Upgrade a package"
                "\n4. Remove an application"
                "\n5. List packages installed with pip"
                "\n6. Credits"
                "\n7. Exit"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Please enter search query: ")
                print(reset + " ")
                os.system(package + " search \"" + user + "\"")

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print(reset + "")
                os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Please enter which package(s) to upgrade: ")
                print(reset + "")
                os.system(package + " install --upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print(reset + "")
                os.system(package + " uninstall \"" + user + "\"")
                askreturn()

            if user == "5":  # List
                clear()
                print(reset + "")
                user = input(multichoicePrompt(
                    "Please choose an action:\n"
                    "\n1. List all packages"
                    "\n2. List outdated packages"))
                if user == "1": os.system(package + " list ")
                if user == "2": os.system(package + " list --outdated")
                askreturn()

            if user == "6":  # Credits
                clear()
                print(credit)
                time.sleep(3)
                clear()

            if user == "7":
                print(reset)
                quit()

    if package == "apm":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Upgrade a package"
                "\n4. Remove an application"
                "\n5. List packages installed"
                "\n6. Credits"
                "\n7. Exit"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Please enter search query: ")
                print("")
                os.system("apm search " + user)

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print("")
                os.system("apm install " + user)

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Please enter which package(s) to upgrade: ")
                print("")
                os.system(reset + "apm upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print("")
                os.system(reset + "apm uninstall" + user)

                askreturn()

            if user == "5":  # List
                clear()
                print("")
                user = input(multichoicePrompt(
                    "Please choose an action:\n"
                    "\n1. List all packages"
                    "\n2. List outdated packages"))
                if user == "1": os.system("apm list")
                if user == "2": os.system("apm outdated")
                askreturn()

            if user == "6":  # Credits - Meooow
                clear()
                print(credit)
                
                askreturn()

            if user == "7":
                print(reset)
                quit()
                
except KeyboardInterrupt:
        clear()
        print(red + "Error: Keyboard Interuption. Quitting" + reset) # moo
        quit()
