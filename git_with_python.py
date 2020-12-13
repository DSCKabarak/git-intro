# understanding git with python scripts

# check CPU usage automation

import psutil

def check_cpUsage(percentage):
    usage = psutil.cpu_percent()
    return usage < percentage

    if not check_cpUsage(75):
        print("ERROR CPU overload !!!")
    else:
        print("Everythin OK")
