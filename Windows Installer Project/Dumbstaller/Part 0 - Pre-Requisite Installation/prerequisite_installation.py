#-------------------------------pseudocode---------------------------------------
# check running environment.
#   the computer must connect to the internet. if not display a message.
# change the name of the computer (ask user) and restart computer.
#   skip if the computer already joined a domain.
# restart the computer ONLY if the pre-requisite runs smoothly.

#-------------------------------------------------------------------------------

# import space
import os, re, subprocess
import admin
from sys import exit # used to cleanly exit the script

if not admin.isUserAdmin(): # if user is not admin then run as admin
    admin.runAsAdmin()


# a function called internet_check to check for internet connection
def internet_check():
    server = "google.com" # server to ping to
    response = os.system("ping " + server)  # ping the server

    if response == 0:
        return True # if response value is 0, there is an internet connection
    else:
        return False # if response value is 1, there isn't an internet connection



# a function called hostname_change to change hostname
# must run this as administrator as it has to call powershell for administrative
# task (changing host name is an administrative task)
def hostname_change(hostname):
    subprocess.call(['powershell.exe', "Rename-Computer -NewName " + hostname])



# make sure the hostname is acceptable by the OS
def check_name(hostname):
    pattern = r'[^A-Za-z0-9]'  # anything but letters and numbers

    if not hostname: # empty string False
        return False
    if re.search(pattern, hostname): # anything else besides words False
        return False
    else:  # if it contains just letters True
        return True



# a function called restart_computer to restart the computer
def restart_computer():
    subprocess.call(['powershell.exe', "shutdown /r /t 0"])



# main function
def main():

    print("\nWelcome! This program will check your PC environment before you can install software.\n")

    print("Check for an Internet connection...")

    if internet_check(): # if there is an Internet connection
        print("\nInternet connection detected!")

        # ask user if he/she wishes to change the host name
        print("\nYou can exit the program and start Part 1 now if you don't want to change your host name.")
        temp_input = input("Do you want to exit?(y/n): ").lower()

        # input check and final decision
        while temp_input != "y" and temp_input != "n": # if input != y or n
            print("Unacceptable input!")
            temp_input = input("Do you want to exit?(y/n): ").lower()

        if temp_input == "y": # if the user wants to exit
            exit()

        else: # if the user doesn't want to exit

            # change host name and restart Windows
            print("\nNow, you need to think of a cool name for your PC!")
            hostname = input("Please choose a name for your PC: ")

            # a small check to make sure the new host name is acceptable
            while check_name(hostname) == False: # keep asking until acceptable
                print("This name is unacceptable. Please try again.")
                hostname = input("Please choose a name for your PC: ")

            print("Name accepted!\n\n")
            hostname_change(hostname) # change host name
            print("Pre-requisite check is finished!")
            input("Press enter to continue...\n")
            print("If you want to change your PC name, please re-run this program.")
            input("Press enter to continue...\n")
            print("You must restart the computer before proceeding to Part 1.")
            input("Press enter to restart...")
            restart_computer() # restart the PC

    else: # if there isn't an Internet connection,
        print("\nInternet connection NOT dectected!")
        print("This program CANNOT run without an internet connection.")
        input("Press enter to exit...")
        exit() # Cleanly closes python script


# run the program
main()


