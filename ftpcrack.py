import ftplib
import os
import wcolors
import sys
options=["0.0.0.0",21,"users.txt","pass.txt"]


def show_options(list):
	print "\nNAME\t\tSETTING\t\tDESCRIPTION"
	print "-----------\t-----------\t--------------"
	print "%s \t\t%s \t%s" % ("Target", list[0], "The Host/IP to attack")
	print "%s \t\t%d \t\t%s" % ("Port", list[1], "Host/IP to attack")
	print "%s \t\t%s \t%s" % ("Users", list[2], "Users Dictionary for try login")
	print "%s \t\t%s \t%s\n" % ("Pass", list[3], "Passwords Dictionary fro try login")	

def conection():
	line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "FuckFtp" + wcolors.color.ENDC
	line_1 += ":"
	line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Brute Force" + wcolors.color.ENDC
	line_1 += " > "
	command = raw_input(line_1)

	if command[0:10] == "set target":
		target = command[11:]
		options[0] = target
		print "Target => ", target
		conection()
	elif command[0:8] == "set port":
		port = command[9:]
		options[1] = int(port)
		print "Port => ", port
		conection()
	elif command [0:13] == "set usersfile":
		usersfile = command[14:]
		options[2] = usersfile
		print "Users File => ", usersfile
		conection()
	elif command [0:12] == "set passfile":
		passfile = command[13:]
		options[3] = passfile
		print "Passwords File => ", passfile
		conection()	
	elif command [0:12] == "show options":
		show_options(options)
		conection()
	elif command [0:4] == "back":
		print "Later!"
		sys.exit()
	else:
		conection()
conection()