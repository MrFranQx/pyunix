def sh(user="root"):     # Define shell function with user defaulting to root
    env = {}      # Initialize empty environment
    
    if user=="root":    # If user is root, set term prefix to # and permissions to true,
        term="# "
        perm=True
    else:               # else set term prefix to $ and permissions to false 
        term="$ "
        perm=False
        
        
    while True:         # main loop
        command=None    # clear command out
        command=input(term).split() # split the command words to list
        command=quotecheck(command) # check if strings present and isolate them
        
        if command==[]: # If command is blank, simply continue
            continue
        else:           # Else run command
            if command[0]=="exit":    # (end session)
                return 0
            
            elif command[0]=="echo":    # (echo a given string or environment variable)
                if len(command)<2:      # If no text given, print out blank space.
                    command.append(" ")
                if command[1][0]=="$":                     # If argument begins with $,
                    if env.get(command[1][1:])==None:      # check if an environment variable exists,
                        print(" ") # if not print blank space and continue
                        continue
                    else:                                  # If a variable exists, print out it value and continue
                        print(env.get(command[1][1:]))
                        continue
                print(*command[1:])                        # Print out given text
                
            elif command[0].count("=")==1:                 # If input contains =, create or update an environment variable
                variable,content=command[0].split("=")
                env.update({variable:content})
                
            elif command[0]=="set":     # (print out entire environment)
                for x in env:
                    print(f'{x}={env[x]}')
            
            else:                       # (print out that command wasn't found)
                print(f"{command[0]}: not found")

def quotecheck(command): # define the string isolating function with given command
    stringcheck=False # informs if string was detected
    arg=[] # list for enclosing the string contents
    stringtype=None # type of quotes (1 – 'single', 2 – "double")
    
    for i in command.copy(): # main loop – operating on copy of command to not destroy original list
        if stringcheck == True: # if inside string, append the word to list
            arg.append(i)
            
        if i.count("'") == 1 and stringcheck==True and stringtype==1: # if at the end of single quote string
            stringcheck = False # set string detector to False
            stringtype = None # unset string type
            arg[0] = arg[0][0:quoteindex]+arg[0][quoteindex+1:] # remove the quote from the beginning word
            arg[-1] = arg[-1][0:i.index("'")]+arg[-1][i.index("'")+1:] # remove the quote from the ending word
            command[startindex] = " ".join(arg) # join the contents of the list and place them in position of first word
            for j in range(len(arg)-1): # loop to remove remaining words
                command.pop(startindex+1)
            arg.clear() # clear the string list
            
        elif i.count("'")==1 and stringcheck==False and stringtype==None: # if at the beginning of single quote string
            startindex = command.index(i) # remember index of first string element
            quoteindex = i.index("'") # remember the position of quote in string
            stringcheck = True # set string detector to True
            stringtype = 1 # set string type to 1 (single quote)
            arg.append(i) # append the first word to list
            
        if i.count('"') == 1 and stringcheck==True and stringtype==2: # if at the end of double quote string
            stringcheck = False # set string detector to False
            stringtype = None # unset string type
            arg[0] = arg[0][0:quoteindex]+arg[0][quoteindex+1:] # remove the quote from the beginning word
            arg[-1] = arg[-1][0:i.index('"')]+arg[-1][i.index('"')+1:] # remove the quote from the ending word
            command[startindex] = " ".join(arg) # join the contents of the list and place them in position of first word
            for j in range(len(arg)-1): # loop to remove remaining words
                command.pop(startindex+1)
            arg.clear() # clear the string list
            
        elif i.count('"')==1 and stringcheck==False and stringtype==None: # if at the beginning of double quote string
            startindex = command.index(i) # remember index of first string element
            quoteindex = i.index('"') # remember the position of quote in string
            stringcheck = True # set string detector to True
            stringtype = 2 # set string type to 2 (double quote)
            arg.append(i) # append the first word to list
            
    return command # return the modified command
