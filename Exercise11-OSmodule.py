# Example file for working with os.path module


import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    
    # Print the name of the OS
    print(os.name)
    
    # Check for items existence and type
    print("Items exists: "+ str(path.exists("textfile.txt")))
    print("Items is a file: "+ str(path.isfile("textfile.txt")))
    print("Items is a directory: "+ str(path.isdir("textfile.txt")))
    
    # Work with file paths
    print("Item path: "+ str(path.realpath("textfile.txt")))
    print("Items path and name: "+ str(path.split(path.realpath("textfile.txt"))))
    
    # Get modification time
    t= time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file has been modified")
    print("Or, " + str(td.total_seconds())+ " seconds")


if __name__ == "__main__":
    main()
    
    
# Prints:
# posix
# Items exists: True
# Items is a file: True
# Items is a directory: False
# Item path: /home/textfile.txt
# Items path and name: ('/home', 'textfile.txt')
# Thu Aug  5 16:12:25 2021
# 2021-08-05 16:12:25.777036
# It has been 0:00:00.047316 since the file has been modified
# Or, 0.047316 seconds
