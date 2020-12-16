import bin.sh # import shell from bin directory

def boot(): # define boot function
    try:
        bin.sh.sh() # run shell
    except EOFError: # if EOF raised, proceed with boot
        pass
