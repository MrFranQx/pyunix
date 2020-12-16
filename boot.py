import sh # import shell

def boot(): # define boot function
    try:
        sh.sh() # run shell
    except EOFError: # if EOF raised, proceed with boot
        pass
