from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import getpass

#Grab credentials
username = raw_input("Enter your username:")
password = getpass.getpass("Enter your password:")

#Confirmation of commands
commands = open("commands" , "r")
commands_to_commit = commands.read()
print ""
print "The commands you are about to commit are: "
print commands_to_commit
print ""
print "Do you want to continue to run these commands?"
confirm = raw_input("Y or N: ")
if confirm in ['n','no','N','NO','No']:
                print "Exiting..."
                quit()
while confirm not in ['y','Y','yes',"Yes",'YES','n','N','NO','No','no']:
        print "Invalid Choice, Try again"
        confirm = raw_input("Y or N: ")
        if confirm in ['n','no','N','NO','No']:
                print "Exiting..."
                quit()
        elif confirm in ['y','Y','yes',"Yes",'YES']:
                continue

#Open a file called swichlist which has a list of devices to modify
with open('switchlist') as infile:
        for host in infile:
                try:
                        print "Working on:", host,
                        #Connect to devices in switchlsit file using username and password provided above
                        dev = Device(host=host.strip(),  user=username, password=password)
                        dev.open()
                        cu = Config(dev)
                        #Looks for a file named commands with the list of commands to run
                        incmd = open('commands')
                        set_cmd = incmd.read()
                        cu.load(set_cmd, format="set")
                        cu.commit()
                        dev.close()
                        print "Completed:", host
                except Exception,e: print "Error:", e
                continue