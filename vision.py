from sys import exit
import time
import tkinter
file = open("Code.vision", "r")
code = file.readlines()
file.close()

for line in code:
    if line[:11] == "OnConsole: ":
        print(line[11:])
    elif line[:13] == "SystemPause: ":
        time.sleep(int(line[13:]))
    elif line[:17] == "OnGUIController: ":
        newScreen = tkinter.Tk()
        newScreen.title(line[17:])
        newScreen.mainloop()
    elif line[:2] == "//":
        print()
    elif line[:0] == "":
        b = 0
    elif line[:1] == " ":
        a = 0
    else:
        print("Code Error: Please Revise Code Block '" + line + "'")
        time.sleep(10)
        exit()
