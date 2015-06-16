from sys import exit
# Importing the exit() function out of sys
import time
# This library helps stop the console for a number of seconds
import tkinter
# The main python graphics library already included in every version of python
file = open("Code.vision", "r")
# Opens up the code you will type
code = file.readlines()
# Gets all the code
file.close()
# Closes the file
for line in code:
    # This scans every line of code
    if line[:11] == "OnConsole: ":
        # Sees if you used OnConsole then prints out the remaining words
        print(line[11:])
        # Look in the previous comment
    elif line[:13] == "SystemPause: ":
        # Sees if you used SystemPause then pauses the console for a number of seconds stated by the coder
        time.sleep(int(line[13:]))
    elif line[:17] == "OnGUIController: ":
        # Scans OnGUIController in your code and then makes a new tkinter screen with the title as the displayed message
        newScreen = tkinter.Tk()
        newScreen.title(line[17:])
        newScreen.mainloop()
    elif line[:2] == "//":
        # Defines the syntax for a comment as in c++, c#, c, java, swift, objective-c, and many other languages
        print()
    elif line[:0] == "":
        # Defines an empty line skipped by the programmer
        b = 0
    elif line[:1] == " ":
        # Same thing as in the last comment
        a = 0
    else:
        # If any other syntax is used, vision gives you an error
        print("Code Error: Please Revise Code Block '" + line + "'")
        time.sleep(10)
        exit()
# End of vision.py
