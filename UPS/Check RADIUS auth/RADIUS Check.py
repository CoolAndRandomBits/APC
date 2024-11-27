# Read a list of IP addresses or hostnames from ups_hosts.txt, try to FTP to each one, and write 
# the results to a file _results.txt


import ftplib
from ftplib import FTP
import sys

print("Please enter the redentials.\n")
print("WARNING: Password will be echoed to screen.  Make sure no one is looking.\n")
strFTPuser = input("Username: ")
strFTPpass = input("Password: ")
print("\n=========================\n")

RecordFile = open("_results.txt", "a")

# Count number of lines

DeviceList = open("ups_hosts.txt", "r")
LineCount = len(DeviceList.readlines())
DeviceList.close()

# Reopen the file for processing

DeviceList = open("ups_hosts.txt", "r")
Counter = 0

# Iterate through the file

while Counter < LineCount:

        Host = str(DeviceList.readline().rstrip())

        print("Processing %s" %Host)


        try:
                FTPconn = FTP(Host)
                FTPconn.login(strFTPuser,strFTPpass)
                print(FTPconn.welcome)
                print("Successfully logged into %s" %Host)
                RecordFile.write("\n%s,%s,Success" %(Host, FTPconn.welcome))
        except ftplib.error_perm as e:
                print(e.args[0])
                print("Failed to login to %s" %Host)
                RecordFile.write("\n%s,%s,Failed" %(Host, e))

        RecordFile.flush()

        print("Processing %s complete\n" %Host)
        print("=========================\n")

        Counter += 1
        

        FTPconn.close()


DeviceList.close()
RecordFile.close()


