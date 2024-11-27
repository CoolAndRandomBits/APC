# Read a list of IP addresses or hostnames from ups_hosts.txt, try to FTP to each one, and 
# send the .ini config file to it 


from ftplib import FTP
import sys

print("Please enter the credentials.\n")
print("WARNING: Password will be echoed to screen.  Make sure no one is looking.\n")
strFTPuser = input("Username: ")
strFTPpass = input("Password: ")


def FTPtoHost(argFTPhost):
	# This function will transfer the config file to the UPS

        objFTP = FTP(argFTPhost)
        print(objFTP.welcome)


        objFTP.login(strFTPuser,strFTPpass)

        objFTP.storbinary("STOR config.ini", open("config.ini", "rb"), 1024)
        print("Uploaded file")
        objFTP.close()



def main():
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

                
                FTPtoHost(Host)
        

                print("Processing %s complete\n" %Host)
                print("=========================\n")

                Counter += 1

        DeviceList.close()

main()
