targetDrive="D:"
sourceDrive="C:"

print(targetDrive+"/Program Files/GIGABYTE")

##Installer Function
import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def gigabyteInstaller():
    if make_sure_path_exists(targetDrive+"/Program Files/GIGABYTE")==False:
        os.mkdir(targetDrive+"/Program Files/GIGABYTE")
    os.symlink(targetDrive+"/Program Files/GIGABYTE",sourceDrive+"/Program Files/GIGABYTE")
    if make_sure_path_exists(targetDrive+"/Program Files (x86)/GIGABYTE")==False:
        os.mkdir(targetDrive+"/Program Files (x86)/GIGABYTE")
    os.symlink(targetDrive+"/Program Files (x86)/GIGABYTE",sourceDrive+"/Program Files (x86)/GIGABYTE")
    return;

##Main Loop
gigabyteInstaller()
