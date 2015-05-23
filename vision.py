import time
file = open("MyCode.lang", "r")
read = file.readlines()
file.close()
length = read.__len__()
for i in range(length):
    getCodeOnLine = read[i-1]
    if getCodeOnLine[:11] == 'OnConsole: ':
        print(getCodeOnLine[11:])
    if getCodeOnLine[:13] == 'SystemPause: ':
        time.sleep(int(getCodeOnLine[13:]))
