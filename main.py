#!/bin/python3

import unix # import main pyunix module

while True: # main loop
    try:
        boot = input("@ ") # display prompt
        if boot=="unix" or boot=="boot": # if entered "unix" or "boot" run unix, then exit
            unix.unix()
            print("\n")
            exit(0)
        else: # else print "Unknown operation"
            print("Unknown operation")
    except (EOFError): # if EOF raised, exit normally
        print("\n")
        exit(0)
