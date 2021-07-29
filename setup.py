import time

"""
This file is mostly for setting up the project.

It'll ask the end user for a few parameters and messages they wish to be sent. These are stored in plaintext in the
Messages folder.

It is necessary to populate the .txt files, as the publisher will refuse to run (by design) if any of the .txt files are blank ("")
"""


print("Hello, and welcome to this doorbell software.\n")
time.sleep(1)
print("Please use this setup file to set up the messages you would like the doorbell to send.\n")
time.sleep(1)

i = 0
def confirmation(finished, msginput):
    
    while(~finished):
        print(f"Your desired message is \"{msginput}\"? (y/n)")
        yn = input()
        if yn == "y":
            global i
            f.write(msginput)
            f.close()
            i = i+1
            finished = True
            return 
        elif yn == "n":
            finished = False
            f.close()
            PressDef(finished)
            return
        else:
            print("Please enter a valid input.")
            finished = False
            
def PressDef(finished):
    global f
    global i
    f = open(f"Messages/message{i}.txt", 'w')
    if(i == 0):
        print("Please enter your desired message for a short press.")
    elif(i == 1):
        print("Please enter your message for a long press.")
    elif(i == 2):
        print("Please enter your message for two presses.")
    msginput = input()
    confirmation(finished, msginput) # Throws a "Are you sure?" to the user.
    return

    
finished = False
message = PressDef(finished)
finished = False
message = PressDef(finished)
finished = False
message = PressDef(finished)

print("Setup is complete. Please run the doorbell main.")
