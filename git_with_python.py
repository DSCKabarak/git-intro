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

# =======================================latetest commit

### Disk Low usage
### The Error code is return is outside the function
import shutil

def check_disk_usage(disk,min_abs,min_percent):
    du = shutil.disk_usage(disk)
    #calc % of free space
    percent_free = 100*du.free/du.total
    #calc free bytes
    gb_free = du.free/2**30
    if percent_free < min_percent or gb_free < min_abs:
        return False
    return True
#check for 2GB and atleast 10% free
if not check_disk_usage("/",2*2**30,10):
    print("Error: Clean some space")
    return 1
print("All ok, Proceed with execution")
return 0

#soln 1 fix and run changes
import shutil
import sys

def check_disk_usage(disk,min_abs,min_percent):
    du = shutil.disk_usage(disk)
    #calc % of free space
    percent_free = 100*du.free/du.total
    #calc free bytes
    gb_free = du.free/2**30
    if percent_free < min_percent or gb_free < min_abs:
        return False
    return True
#check for 2GB and atleast 10% free
if not check_disk_usage("/",2*2**30,10):
    print("Error: Clean some space")
    sys.exit(1)
print("All ok, Proceed with execution")
sys.exit(0)


## fix error 2, stop calling the conversion twice
import shutil
import sys

def check_disk_usage(disk,min_abs,min_percent):
    du = shutil.disk_usage(disk)
    #calc % of free space
    percent_free = 100*du.free/du.total
    #calc free bytes
    gb_free = du.free/2**30
    if percent_free < min_percent or gb_free < min_abs:
        return False
    return True
#check for 2GB and atleast 10% free
if not check_disk_usage("/",2,10):
    print("Error: Clean some space")
    sys.exit(1)
print("All ok, Proceed with execution")
sys.exit(0)
